from odoo import fields, models


class Mission(models.Model):
    _name = 'space_mission.mission'
    _description = 'Model for Space Mission'

    name = fields.Char(string="Name of the mission", required=True)
    spaceship_id = fields.Many2one(
        "space_mission.spaceship", string="Spaceship", required=True
    )
    crew_ids = fields.Many2many("res.partner", "crew_partner_rel")
    project_ids = fields.Many2many("project.project", "project_mission_rel")
    launch_date = fields.Datetime(string="Launch of the mission", required=True)
    return_date = fields.Datetime(string="Return of the mission", required=True)
    # metrics
    fuel_consumed = fields.Float(string="Fuel Consumed", default=0.0)
    engines = fields.Integer(string="Number of engines", default=1)
    accidents = fields.Integer(string="Accidents on mission", default=0)
