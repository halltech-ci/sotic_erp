# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class hta_custom_employee(models.Model):
#     _name = 'hta_custom_employee.hta_custom_employee'
#     _description = 'hta_custom_employee.hta_custom_employee'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
