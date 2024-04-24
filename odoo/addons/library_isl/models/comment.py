from odoo import models,fields

class CommentModel (models.model) :
    _name='a.commentmodel'

    comment_id=fields.Many2one('a.bookmodel','')