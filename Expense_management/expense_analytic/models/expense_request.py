# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ExpenseRequest(models.Model):
    _inherit = 'expense.request'
    
    analytic_account = fields.Many2one('account.analytic.account', string='Analytic Account', check_company=True,)
    
    def create_bank_statement(self):
        res = super(ExpenseRequest, self).create_bank_statement()
        return res    
    
    
class ExpenseLine(models.Model):
    _inherit = "expense.line"
    
    @api.model
    def _get_analytic_domain(self):
        project_ids = self.env['project.project'].search([]).ids
        res = [('project_ids', 'not in', project_ids)]
        return res
    
    
    @api.model
    def _get_project_domain(self):
        project_ids = self.env['project.project'].search([]).ids
        res = [('id', 'in', project_ids)]
        return res
    
    
    analytic_account = fields.Many2one('account.analytic.account', string='Analytic Account', dpmain=lambda self:self._get_analytic_domain())
    project = fields.Many2one('project.project', string='Project', domain=lambda self: self._get_project_domain())
    expense_type = fields.Boolean(string="Imputer au projet", default=True)
    
    
    def _get_statement_line(self):
        vals = super(ExpenseLine, self)._get_statement_line()
        vals['analytic_account'] = self.analytic_account.id
        return vals