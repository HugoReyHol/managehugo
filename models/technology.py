from odoo import fields, models, api


class technology(models.Model):
    _name = 'managehugo.technology'
    _description = 'managehugo.technology'

    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
    photo = fields.Image(string='Foto')
