from odoo import models, fields, api


class history(models.Model):
    _name = 'managehugo.history'
    _description = 'managehugo.history'

    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
