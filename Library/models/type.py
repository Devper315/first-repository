from odoo import models, fields, api


class Type(models.Model):
    _name = "type"
    _description = "Type Infomation"

    name = fields.Char(string="Tên", required=1)