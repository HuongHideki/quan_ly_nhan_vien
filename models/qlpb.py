# -*-coding: utf-8 -*-

from odoo import models, fields

class QuanLyPhongBan(models.Model):
    _name = 'quanly.phongban'
    _description = 'Quan Ly manage_department'

    name = fields.Char('Tên', size=225, required=True)
    code = fields.Char('Mã', size=50, required=True)
    describe = fields.Text('Mô tả', size =1000)
    m2m = fields.Many2many('quanly.nhanvien', string="Thêm nhân viên")