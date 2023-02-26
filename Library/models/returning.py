from odoo import models, api, fields


class Returning(models.Model):
    _name = 'returning'
    _description = 'Returing Transaction Infomation'

    borrowing_id = fields.One2many(comodel_name='borrowing', inverse_name='returning_id')