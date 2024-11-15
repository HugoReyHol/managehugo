from odoo import models, fields, api


class project(models.Model):
    _name = 'managehugo.project'
    _description = 'managehugo.project'

    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
