from odoo import fields, models


class Project(models.Model):
    _inherit = "project.project"

    mission_ids = fields.One2many(
        "space_mission.mission", "project_ids", string="Related Mission"
    )
