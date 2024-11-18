from odoo import models, fields, api


class task(models.Model):
    _name = 'managehugo.task'
    _description = 'managehugo.task'

    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
    start_date = fields.Datetime(string="Fecha comienzo")
    end_date = fields.Datetime(string="Fecha final")
    is_paused = fields.Boolean(string='Pausado')

    # Relaciones entre tablas
    sprint_id = fields.Many2one(comodel_name="managehugo.sprint", string="Sprint", required=True, ondelete="cascade")
    technologies_ids = fields.Many2many(comodel_name='managehugo.technology',
                                        string='Technologies',
                                        relation='tasks_technologies',
                                        column1="technologies_ids",
                                        column2="tasks_ids")

    history_id = fields.Many2one(
        comodel_name='managehugo.history',
        string='History',
        required=False)
    