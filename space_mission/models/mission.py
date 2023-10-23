from odoo import api, fields, models, _


class Mission(models.Model):
    _name = "space_mission.mission"
    _description = "Model for Space Mission"

    name = fields.Char(string="Name of the mission", required=True)
    spaceship_id = fields.Many2one(
        "space_mission.spaceship", string="Spaceship", required=True
    )
    state = fields.Selection(
        selection=[
            ("canceled", "Canceled"),
            ("draft", "Draft"),
            ("scheduled", "Scheduled"),
            ("in_progress", "In Progress"),
            ("done", "Done"),
        ],
        string="Status",
        required=True,
        default="draft",
    )
    color = fields.Char(string="Color of the Spaceship", compute="_compute_color")
    crew_ids = fields.Many2many("res.partner", "crew_partner_rel")
    project_ids = fields.Many2many("project.project", "project_mission_rel")
    project_count = fields.Integer(
        string="Project Count", compute="_compute_project_count"
    )
    launch_date = fields.Datetime(string="Launch of the mission", required=True)
    return_date = fields.Datetime(string="Return of the mission", required=True)
    # metrics
    fuel_consumed = fields.Float(string="Fuel Consumed", default=0.0)
    engines = fields.Integer(string="Number of engines", default=1)
    accidents = fields.Integer(string="Accidents on mission", default=0)

    @api.depends("state")
    def _compute_color(self):
        color_mapping = {
            "cancelled": "danger",
            "draft": "info",
            "scheduled": "warning",
            "in_progress": "primary",
            "done": "success",
        }
        for mission in self:
            mission.color = color_mapping.get(mission.state, "")

    @api.depends("project_ids")
    def _compute_project_count(self):
        for mission in self:
            mission.project_count = len(mission.project_ids)

    def action_get_projects(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Projects"),
            "view_mode": "kanban,tree,graph,form",
            "res_model": "project.project",
            "domain": [("id", "in", self.project_ids.ids)],
        }
