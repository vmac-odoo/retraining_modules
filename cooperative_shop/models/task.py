from odoo import fields, models


class Task(models.Model):
    _name = 'cooperative_shop.task'
    _description = 'Task for Cooperative Shop'

    name = fields.Char()
    start_time = fields.Datetime()
    stop_time = fields.Datetime()
    occurrences = fields.Integer()
    description = fields.Text()
    task_type = fields.Selection([
        ('simple', 'Simple Task'),
        ('complex', 'Complex Task')
    ])
