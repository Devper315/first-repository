from odoo import models, api, fields


class Author(models.Model):
    _name = 'author'
    _description = 'Author Infomation'

    name = fields.Char(string='Tên', required=1)
