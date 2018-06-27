# -*-coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import re


class ManageEmployee(models.Model):
    _name = 'quanly.nhanvien'
    _description = 'Manage Employees'

    code = fields.Char('Code', size=50, required=True)
    name = fields.Char('Name', size=225, required=True)
    describe = fields.Text('Descrition', size =1000)
    email = fields.Char('Email', size=100)
    addr = fields.Text('Address', size=500)
    bdate = fields.Date('Birth Date')
    gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender',default='m')
    cmnd = fields.Char('Peolpe ID', size =12)
    pb_id = fields.Many2one('quanly.phongban', 'Department' )
    m2m = fields.Many2many('quanly.phongban', string="Add Department")
    party = fields.Boolean('Communist Party')
    married = fields.Boolean('Married')
    abc = fields.Boolean('Select All')


    @api.constrains('cmnd')
    def check_cmnd(self):
        if not self.cmnd:
            raise exceptions.ValidationError("Please fill your People ID!")

    @api.onchange('abc')
    def select_all(self):
        if self.abc == 1:
            self.party=1
            self.married=1
        else:
            self.party = 0
            self.married = 0


    @api.constrains('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise exceptions.ValidationError('Not a valid E-mail')