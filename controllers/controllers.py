# -*- coding: utf-8 -*-
# from odoo import http


# class Managehugo(http.Controller):
#     @http.route('/managehugo/managehugo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/managehugo/managehugo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('managehugo.listing', {
#             'root': '/managehugo/managehugo',
#             'objects': http.request.env['managehugo.managehugo'].search([]),
#         })

#     @http.route('/managehugo/managehugo/objects/<model("managehugo.managehugo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('managehugo.object', {
#             'object': obj
#         })
