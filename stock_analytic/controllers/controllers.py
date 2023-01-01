# -*- coding: utf-8 -*-
# from odoo import http


# class StockAnalytic(http.Controller):
#     @http.route('/stock_analytic/stock_analytic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_analytic/stock_analytic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_analytic.listing', {
#             'root': '/stock_analytic/stock_analytic',
#             'objects': http.request.env['stock_analytic.stock_analytic'].search([]),
#         })

#     @http.route('/stock_analytic/stock_analytic/objects/<model("stock_analytic.stock_analytic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_analytic.object', {
#             'object': obj
#         })
