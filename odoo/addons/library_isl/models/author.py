from odoo import models,fields

class AuthorModel(models.Model) :
    _name = 'a.authormodel'

    author_id = fields.One2many('a.bookmodel')
    author_firstname = fields.Char(50)
    author_lasname = fields.Char(50)