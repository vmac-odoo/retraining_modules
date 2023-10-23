from odoo import Command, fields, models


class ProjectTask(models.TransientModel):
    _name = "space_mission.project.task.wizard"
    _description = "Wizard to create a Project from Task"

    def _default_mission(self):
        return self.env["space_mission.mission"].browse(self._context.get("active_id"))

    name = fields.Char(string="Name of the Task", required=True)
    mission_id = fields.Many2one(
        "space_mission.mission",
        string="Mission",
        default=_default_mission,
        required=True,
    )

    def action_create_project(self):
        self.ensure_one()
        new_project = self.env["project.project"].create(
            {"name": self.name, "mission_ids": [Command.link(self.mission_id.id)]}
        )
        return {
            "name": self.name,
            "view_type": "form",
            "view_mode": "form",
            "res_model": "project.project",
            "res_id": new_project.id,
            "type": "ir.actions.act_window",
            "target": "current",
        }
