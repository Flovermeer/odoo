from odoo import models,fields

class CommentModel (models.Model) :
    _name='a.commentmodel'

    #comment_id=fields.Id()
    comment=fields.Text()
    book_id=fields.Integer()