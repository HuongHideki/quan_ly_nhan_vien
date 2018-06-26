# -*-coding: utf-8 -*-

from odoo import models, fields, api

class QuanLyNhanVien(models.Model):
    _name = 'quanly.nhanvien'
    _description = 'Quan Ly Nhan Vien'

    code = fields.Char('Mã', size=50, required=True)
    name = fields.Char('Tên', size=225, required=True)
    describe = fields.Text('Mô tả', size =1000)
    email = fields.Char('Email', size=100)
    addr = fields.Text('Địa Chỉ', size=500)
    bdate = fields.Date('Ngày Sinh')
    gender = fields.Selection([('na', 'Nam'), ('nu', 'Nữ'), ('o', 'Khác')], string='Giới tính',default='na')
    cmnd = fields.Char('Số CMTND', size =12)
    pb_id = fields.Many2one('quanly.phongban', 'Phòng Ban' )
    m2m = fields.Many2many('quanly.phongban', string="Thêm phòng ban")
