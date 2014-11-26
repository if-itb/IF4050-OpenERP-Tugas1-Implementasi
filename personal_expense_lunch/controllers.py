# -*- coding: utf-8 -*-
from openerp import http

# class PersonalExpense(http.Controller):
#     @http.route('/personal_expense/personal_expense/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/personal_expense/personal_expense/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('personal_expense.listing', {
#             'root': '/personal_expense/personal_expense',
#             'objects': http.request.env['personal_expense.personal_expense'].search([]),
#         })

#     @http.route('/personal_expense/personal_expense/objects/<model("personal_expense.personal_expense"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('personal_expense.object', {
#             'object': obj
#         })