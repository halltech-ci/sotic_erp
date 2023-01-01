# -*- coding: utf-8 -*-
# from odoo import http


# class StockRequestAnalytic(http.Controller):
#     @http.route('/stock_request_analytic/stock_request_analytic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_request_analytic/stock_request_analytic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_request_analytic.listing', {
#             'root': '/stock_request_analytic/stock_request_analytic',
#             'objects': http.request.env['stock_request_analytic.stock_request_analytic'].search([]),
#         })

#     @http.route('/stock_request_analytic/stock_request_analytic/objects/<model("stock_request_analytic.stock_request_analytic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_request_analytic.object', {
#             'object': obj
#         })
