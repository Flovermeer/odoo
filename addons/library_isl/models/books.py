from odoo import models,fields, _

class BookModel(models.Model):
   
    _name = 'a.bookmodel'
    _description = 'A little project ISL'
    

    book_id = fields.Id()
    title = fields.Char()
    # NOT USING ISBN as ID because we could have two same examples of the same book #
    isbn = fields.Char()
    author = fields.Integer()
    publication_date = fields.Date()
    owner = fields.Integer()
    books_count = fields.Integer('Books Count', compute='_computed_books_count')
    
    def action_book(self):
        return {
            'title': _('Books'),
            'view_mode': 'tree,form',
            'domain': [('library_isl_book_id', 'in', self.ids)],
            'type': 'ir.actions.act_window',
            'context': {'create': False, 'active_test': False},
            
        }