from odoo import fields, models

class Book(models.Model):
    _name="library.book"
    _description="Book"

    name = fields.Char("Title", required=True)
    publication_date = fields.Integer("Publication date")
    author = fields.Many2one('res.partner', string="Author")
    image = fields.Binary("Cover")
    state = fields.Char("State", default="Available", readonly=True) 
    # readonly = True => éviter que le champ soit éditable dans les vues form


    def rent_book(self):
        if self.state == 'Available':
            self.state = 'Rented'
        else:
            self.state = 'Available'