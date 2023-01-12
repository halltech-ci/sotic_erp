# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit="project.project"
    
    sale_order_ids = fields.One2many("sale.order", inverse_name="project_id", string="Sale Orders", 
                                     #compute="_compute_sale_order_ids", 
                                     store=True
                                    )
    
    #@api.depends('sale_order_id')
    def _compute_sale_order_ids(self):
        for rec in self:
            sales = self.env['sale.order'].search([('project_id', "=", rec.id)])#.mapped('sale_order_id')
            rec.sale_order_ids = sales
