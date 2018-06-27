# -*-coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class WorkingTime(models.Model):
    _name = 'working.time'
    _description = 'Working Time'
    
    start_time = fields.Date('Start Time', default='2000-01-01')
    end_time = fields.Date('End Time', default=fields.Date.today)
    nv_id = fields.Many2one('quanly.nhanvien', 'Employees', required=True)
    pb_id = fields.Many2one('quanly.phongban', 'Department', required=True)
    name = fields.Char(compute='_compute_name')
    email = fields.Char('Email', related='nv_id.email')

    @api.multi
    @api.depends('nv_id', 'pb_id')
    def _compute_name(self):
        for record in self:
            if record.nv_id and record.pb_id:
                record.name = record.nv_id.name + record.pb_id.name

    @api.onchange('start_time')
    def onchange_start_time(self):
        today = fields.Date.today()
        if self.start_time > today:
            raise exceptions.ValidationError("Star time should be less than today!")