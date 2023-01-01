# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProcurementRule(models.Model):
    _inherit = "stock.rule"

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values,):
        res = super(ProcurementRule, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values,)
        if values.get("stock_request_id"):
            stock_request = self.env["stock.request"].browse(values["stock_request_id"])
            analytic_account = stock_request.analytic_account_id
            analytic_tags = stock_request.analytic_tag_ids
            res.update(
                analytic_account_id=analytic_account.id,
                analytic_tag_ids=[(4, tag.id) for tag in analytic_tags],
            )
        return res
