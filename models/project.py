from odoo import models, fields, api


class project(models.Model):
    _name = 'managehugo.project'
    _description = 'managehugo.project'

    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')

    # Relaciones entre tablas
    histories_ids = fields.One2many(
        comodel_name='managehugo.history',
        inverse_name='project_id',
        string='Histories',
        required=False)

    sprints_ids = fields.One2many(
        comodel_name='managehugo.sprint',
        inverse_name='project_id',
        string='Sprints',
        required=False)
