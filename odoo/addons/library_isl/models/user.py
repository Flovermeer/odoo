from odoo import models,fields

class UserModel (models.Model) :
    
    _name = 'a.usermodel'
    _description = 'User table'


    user_id = fields.Id()
    last_name = fields.Char()
    first_name = fields.Char()
    email = fields.Char() #todo : contrainte unique

    books = fields.One2many('a.bookmodel','a.bookmodel.book_id',string='Livres')