# -*- coding: utf-8 -*-
from odoo import http

# class Kedamos(http.Controller):
#     @http.route('/kedamos/kedamos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kedamos/kedamos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kedamos.listing', {
#             'root': '/kedamos/kedamos',
#             'objects': http.request.env['kedamos.kedamos'].search([]),
#         })

#     @http.route('/kedamos/kedamos/objects/<model("kedamos.kedamos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kedamos.object', {
#             'object': obj
#         })