# -*-coding: utf-8 -*-

from odoo import models, fields

class ManageDepartment(models.Model):
    _name = 'quanly.phongban'
    _description = 'manage_department'

    name = fields.Char('Name', size=225, required=True)
    code = fields.Char('Code', size=50, required=True)
    describe = fields.Text('Descrition', size =1000)
    m2m = fields.Many2many('quanly.nhanvien', string="Add Employee")