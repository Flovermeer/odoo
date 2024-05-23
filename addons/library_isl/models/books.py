from odoo import models,fields

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
    

