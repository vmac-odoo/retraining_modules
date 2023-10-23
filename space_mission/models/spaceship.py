from odoo import api, fields, models, _
from odoo.exceptions import UserError


class Spaceship(models.Model):
    _name = "space_mission.spaceship"
    _description = "Record for spaceship metrics"

    name = fields.Char()
    active = fields.Boolean(default=True)
    type = fields.Selection(
        [
            ("freighter", "Freighter"),
            ("transport", "Transport"),
            ("scout_ship", "Scout Ship"),
            ("fighter", "Fighter"),
        ]
    )
    model = fields.Char(required=True)
    build_date = fields.Date()
    captain = fields.Char()
    required_crew = fields.Integer()
    length = fields.Float()
    width = fields.Float()
    height = fields.Float()
    engine_number = fields.Char()
    fuel_type = fields.Selection(
        [("solid_fuel", "Solid Fuel"), ("liquid_fuel", "Liquid Fuel")]
    )
    mission_ids = fields.One2many("space_mission.mission", "spaceship_id")
    mission_count = fields.Integer(string="Number of missions", compute="_compute_mission_count")

    @api.constrains
    def validate_dimensions(self):
        for spaceship in self:
            if spaceship.width > spaceship.length:
                raise UserError(_("Width must be greater than length"))

    @api.depends('mission_ids')
    def _compute_mission_count(self):
        for spaceship in self:
            spaceship.mission_count = len(spaceship.mission_ids)

    def action_get_missions(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Missions"),
            "view_mode": "kanban,tree,form",
            "res_model": "space_mission.mission",
            "domain": [("id", "in", self.mission_ids.ids)],
        }
