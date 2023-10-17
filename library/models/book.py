from odoo import fields, models


class Book(models.Model):
    _name = "library.book"
    _description = "Library Book"

    name = fields.Char()
    active = fields.Boolean(default=True)
    isbn = fields.Char()
    genre = fields.Char()
    summary = fields.Text()
    author = fields.Char()
    format = fields.Selection(
        [
            ("paperback", "Paperback"),
            ("hardcover", "Hardcover"),
            ("audiobook", "Audiobook"),
            ("ebook", "E-book"),
        ]
    )
    language = fields.Selection(
        [("en", "English"), ("es", "Spanish"), ("fr", "French"), ("de", "Deutsch")]
    )
    edition = fields.Integer()
    publisher = fields.Char()
    publish_date = fields.Date()
    company_id = fields.Many2one(
        "res.company",
        store=True,
        copy=False,
        string="Company",
        default=lambda self: self.env.user.company_id.id,
    )
    currency_id = fields.Many2one(
        "res.currency",
        string="Currency",
        related="company_id.currency_id",
        default=lambda self: self.env.user.company_id.currency_id.id,
    )
    price = fields.Monetary()
