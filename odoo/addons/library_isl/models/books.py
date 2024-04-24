from odoo import models,fields

class BookModel(models.Model):
   
    _name = 'a.bookmodel'
    _description = 'A little project ISL'
    

    book_id = fields.Id()
    title = fields.Char()
    # NOT USING ISBN as ID because we could have two same examples of the same book #
    isbn = fields.Char()
    author = fields.Many2one('a.authormodel','a.authormodel.author_id',string='Nom de l\'auteur')
    publication_date = fields.Date()
    comments = fields.One2many('a.commentmodel','a.commentmodel.comment_id',string='Commentaires')
    
    owner = fields.Many2one('a.usermodel','a.usermodel.user_id',)
    

