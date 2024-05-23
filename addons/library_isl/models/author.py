from odoo import models,fields

class AuthorModel(models.Model) :
    _name = 'a.authormodel'

    #author_id = fields.Id()
    author_firstname = fields.Char()
    author_lastname = fields.Char()