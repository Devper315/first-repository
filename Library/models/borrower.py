from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError


class Borrower(models.Model):
    _name = 'borrower'
    _description = 'Borrower Infomation'

    name = fields.Char(string='Tên', required=1)
    date_of_birth = fields.Date(string='Ngày sinh')
    gender = fields.Selection(required=1, string='Giới tính',
                              selection=[('male', 'Nam'), ('female', 'Nữ')])
    phone = fields.Char(string='SĐT', required=1)
    email = fields.Char(string='Email')
    borrowing_ids = fields.One2many(comodel_name='borrowing', inverse_name='borrower_id', required=1, readonly=1)

    @api.constrains('phone')
    def validate_phone(self):
        for borrower in self:
            if not borrower.phone.isdigit() or len(borrower.phone) < 10:
                raise ValidationError('Số điện thoại không hợp lệ')

    @api.model
    def create(self, vals):
        if vals.get('name', False):
            vals['name'] = vals['name'].title()
        return super(Borrower, self).create(vals)

    def write(self, vals):
        if vals.get('name', False):
            vals['name'] = vals['name'].title()
        return super(Borrower, self).write(vals)
    
    def unlink(self):
        for borrower in self:
            if len(borrower.borrowing_ids) > 0:
                raise ValidationError('Không thể xóa khách hàng đang mượn sách')
        return super(Borrower, self).unlink()