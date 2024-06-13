from odoo import models, fields

class User(models.Model):
    _inherit = 'res.users'

    borrowed_books_ids = fields.One2many('library_isl.book.tracking', 'borrower_id', string='Borrowed Books')