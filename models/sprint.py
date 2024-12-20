from odoo import models, fields, api
import datetime


class sprint(models.Model):
    _name = 'managehugo.sprint'
    _description = 'managehugo.sprint'

    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
    duration = fields.Integer(string='Duración', default=15)
    start_date = fields.Datetime(string="Fecha comienzo")
    end_date = fields.Datetime(string="Fecha final", compute="_get_end_date", store=True)

    # RELACIÓN TABLAS
    tasks_ids = fields.One2many(string='Tasks', comodel_name="managehugo.task", inverse_name="sprint_id")

    project_id = fields.Many2one(
        comodel_name='managehugo.project',
        string='Project',
        required=False,
        ondelete="cascade")

    # CAMPOS COMPUTADOS
    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for sprint in self:
            if isinstance(sprint.start_date, datetime.datetime) and sprint.duration > 0:
                sprint.end_date = sprint.start_date + datetime.timedelta(days=sprint.duration)
            else:
                sprint.end_date = sprint.start_date
