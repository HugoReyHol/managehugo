from odoo import models, fields, api


class sprint(models.Model):
    _name = 'managehugo.sprint'
    _description = 'managehugo.sprint'

    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
    start_date = fields.Datetime(string="Fecha comienzo")
    end_date = fields.Datetime(string="Fecha final")

    # RELACIÓN TABLAS
    tasks_ids = fields.One2many(string='Tasks', comodel_name="managehugo.task", inverse_name="sprint_id")
