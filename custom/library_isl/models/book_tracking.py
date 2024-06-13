from odoo import models, fields

class BookTracking(models.Model):
    _name = 'library_isl.book.tracking'
    _description = 'Book Tracking'

    book_id = fields.Many2one('library_isl.book', string='Book', required=True)
    borrower_id = fields.Many2one('res.users', string='Borrower', required=True)
    borrow_date = fields.Datetime(string='Borrow Date', default=fields.Datetime.now)
    return_date = fields.Datetime(string='Return Date')