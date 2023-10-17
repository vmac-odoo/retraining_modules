from odoo import fields, models


class Spaceship(models.Model):
    _name = 'space_mission.spaceship'
    _description = 'Record for spaceship metrics'

    name = fields.Char()
    active = fields.Boolean(default=True)
    type = fields.Selection([
        ('freighter', 'Freighter'),
        ('transport', 'Transport'),
        ('scout_ship', 'Scout Ship'),
        ('fighter', 'Fighter')
    ])
    model = fields.Char(required=True)
    build_date = fields.Date()
    captain = fields.Char()
    required_crew = fields.Integer()
    length = fields.Float()
    width = fields.Float()
    height = fields.Float()
    engine_number = fields.Char()
    fuel_type = fields.Selection([
        ('solid_fuel', 'Solid Fuel'),
        ('liquid_fuel', 'Liquid Fuel')
    ])
