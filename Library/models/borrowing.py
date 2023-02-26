from odoo import models, fields, api


class Borrowing(models.Model):
    _name = 'borrowing'
    _description = 'Borrowing Transaction Infomation'

    book_ids = fields.Many2many(comodel_name='book', relation='book_borrowing_rel',
                                    column2='book_id', column1='borrowing_id', string='Tên sách', required=1)
    employee_id = fields.Many2one(comodel_name='employee', string='Nhân viên cho mượn', required=1)
    borrower_id = fields.Many2one(comodel_name='borrower', string='Người mượn', required=1)
    borrowing_date = fields.Date(string='Ngày mượn', required=1, readonly=1)
    state = fields.Selection(string='Trạng thái',
                              selection=[('yes', 'Đã trả'), ('no', 'Chưa trả')], required=1)
    on_demand_returning_date = fields.Date(string='Hạn trả')
    returning_id = fields.Many2one(comodel_name='returning')