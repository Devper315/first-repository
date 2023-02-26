from odoo import models, api, fields


class Publisher(models.Model):
    _name = 'publisher'
    _description = 'Publisher Infomation'

    name = fields.Char(string='Tên', required=1)