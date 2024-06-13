from odoo import models, fields

class Book(models.Model):
    _name = 'library_isl.book'
    _description = 'Book'

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    isbn = fields.Char(string='ISBN')
    owner_id = fields.Many2one('res.users', string='Owner', required=True)
    book_tracking_ids = fields.One2many('library_isl.book.tracking', 'book_id', string='Book Tracking')