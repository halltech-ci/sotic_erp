# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    
    order_type = fields.Many2one('sale.order.type', string="Domaine")
    sequence_code = fields.Char(string='Sequence Code', default='sale.order',)
    
    @api.depends('order_type.ir_sequence')
    def _compute_sequence_code(self):
        for order in self:
            if order.order_type:
                order.sequence_code = order.order_type.ir_sequence.code
            else:
                order.sequence_code = 'sale.order'
                
    @api.onchange('order_type')
    def _onchange_order_type(self):
        if self.order_type:
            self.sequence_code = self.order_type.ir_sequence.code
        else:
            self.sequence_code = 'sale.order'
    
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            next_code = 'sale.order'
            domain_code = vals.get('sequence_code')
            if domain_code != 'sale.order':
                next_code = domain_code
            if 'date_order' in vals:
                seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
            if 'company_id' in vals:
                vals['name'] = self.env['ir.sequence'].with_context(with_company=vals['company_id']).next_by_code(
                    next_code, sequence_date=seq_date) or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code(next_code, sequence_date=seq_date) or _('New')
        # Makes sure partner_invoice_id', 'partner_shipping_id' and 'pricelist_id' are defined
        if any(f not in vals for f in ['partner_invoice_id', 'partner_shipping_id', 'pricelist_id']):
            partner = self.env['res.partner'].browse(vals.get('partner_id'))
            addr = partner.address_get(['delivery', 'invoice'])
            vals['partner_invoice_id'] = vals.setdefault('partner_invoice_id', addr['invoice'])
            vals['partner_shipping_id'] = vals.setdefault('partner_shipping_id', addr['delivery'])
            vals['pricelist_id'] = vals.setdefault('pricelist_id', partner.property_product_pricelist and partner.property_product_pricelist.id)
        result = super(SaleOrder, self).create(vals)
        return result