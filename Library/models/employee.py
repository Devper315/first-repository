from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Employee(models.Model):
    _name = 'employee'
    _description = 'Employee Infomation'

    name = fields.Char(string='Tên', required=1)
    date_of_birth = fields.Date(string='Ngày sinh', required=1)
    phone = fields.Char(string='SĐT', required=1)
    email = fields.Char(string='Email')
    state = fields.Selection(string='Trạng thái',
                             selection=[('on board', 'Đang làm việc'), ('leave', 'Đã nghỉ')])
    borrowing_ids = fields.One2many(comodel_name='borrowing', inverse_name='employee_id', string='Giao dịch', required=1)

    @api.constrains('phone')
    def validate_phone(self):
        for borrower in self:
            if not borrower.phone.isdigit() or len(borrower.phone) < 10:
                raise ValidationError('Số điện thoại không hợp lệ')

    @api.model
    def unlink(self):
        for employee in self:
            if employee.state == 'on board':
                raise ValidationError('Không thể xóa nhân viên còn làm việc')
        return super(Employee, self).unlink()
            