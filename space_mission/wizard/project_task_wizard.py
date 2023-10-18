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
        self.env["project.project"].create(
            {"name": self.name, "mission_ids": [Command.link(self.mission_id.id)]}
        )
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": "Project Created",
                "message": f"Project for mission(s) has been created successfully.",
                "type": "success",
                "sticky": False,
            },
        }
