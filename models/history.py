from odoo import models, fields, api


class history(models.Model):
    _name = 'managehugo.history'
    _description = 'managehugo.history'

    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')

    # Relaciones entre tablas
    project_id = fields.Many2one(
        comodel_name='managehugo.project',
        string='Project',
        required=False,
        ondelete="cascade")
