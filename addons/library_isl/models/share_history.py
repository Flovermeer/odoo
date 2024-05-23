from odoo import models, fields

class ShareHistoryModel(models.Model):

    _name = 'a.sharehistorymodel'
    _description = 'Historique des partages'

    id = fields.Id()
    inbox_date = fields.Date()
    take_out_date = fields.Date()

    book_id = fields.Integer()
    user_id = fields.Integer()