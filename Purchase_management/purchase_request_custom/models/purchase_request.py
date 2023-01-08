# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PurchaseRequest(models.Model):
    _inherit = "purchase.request"
    
    
    @api.model
    def _get_default_name(self):
        return self.env["ir.sequence"].next_by_code("purchase.request")
    
    
    name = fields.Char(string="Request Reference", required=True, default='/', index=True, readonly=True)
    request_date = fields.Datetime(string="Request date", help="Date when the user initiated the request.", default=fields.Datetime.now, tracking=True, readonly=True)
    

class PurchaseRequestLine(models.Model):
    _inherit = 'purchase.request.line'
    
    product_tmpl_id = fields.Many2one("product.template", related="product_id.product_tmpl_id", store=True)
    attribute_line_ids = fields.One2many("product.template.attribute.line", related="product_tmpl_id.attribute_line_ids")
    specifications = fields.Text(default="")