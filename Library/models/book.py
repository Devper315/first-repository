from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = 'book'
    _description = 'Book Infomation'

    name = fields.Char(string='Tên', required=1)
    type_ids = fields.Many2many(comodel_name='type', relation='book_type_rel',
                               column1='book_id', column2='type_id', string='Thể loại', required=1)
    author_ids = fields.Many2many(comodel_name='author', relation='book_author_rel',
                              column1='book_id', column2='author_id', string='Tác giả', required=1)
    publisher_id = fields.Many2one(comodel_name='publisher', string='NXB', required=1)
    borrowing_ids = fields.Many2many(comodel_name='borrowing', relation='book_borrowing_rel',
                                    column1='book_id', column2='borrowing_id', string='Danh sách người mượn', readonly=1)
    total_quantity = fields.Integer(string='Tổng số lượng')
    rest_quantity = fields.Integer(string='Số lượng còn lại', compute='get_rest_quantity')
    first_import_date = fields.Date(string='Ngày nhập đầu tiên')
    number_of_borrower = fields.Integer(string='Số lượng người mượn', compute='get_number_of_borrower', required=1)
    image_1920 = fields.Image(string="Ảnh", max_width=1920, max_height=1920)
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)

    @api.depends('borrowing_ids')
    def get_number_of_borrower(self):
        for book in self:
            book.number_of_borrower = len(book.borrowing_ids)

    @api.depends('number_of_borrower')
    def get_rest_quantity(self):
        for book in self:
            book.rest_quantity = book.total_quantity - book.number_of_borrower

    @api.model
    def create(self, vals):
        if vals.get('name', False):
            s = vals['name']
            s = s[0].upper()+s[1:].lower()
            vals['name'] = s
        return super(Book, self).create(vals)

    def write(self, vals):
        if vals.get('name', False):
            s = vals['name']
            s = s[0].upper()+s[1:].lower()
            vals['name'] = s
        return super(Book, self).write(vals)

    def unlink(self):
        # for book in self:
        #     if len(book.borrower_ids)>0:
        #         raise ValidationError('Không thể xóa sách đang có người mượn')
        return super(Book, self).unlink()