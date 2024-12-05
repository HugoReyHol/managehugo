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

    tasks_ids = fields.One2many(
        comodel_name='managehugo.task',
        inverse_name='history_id',
        string='Tasks',
        required=False)

    used_technologies = fields.Many2many(
        comodel_name='managehugo.technology',
        string='Tecnologías usadas',
        compute="_get_used_technologies")

    # CAMPOS COMPUTADOS
    def _get_used_technologies(self):
        for history in self:
            technologies = None

            for task in history.tasks_ids:
                if not technologies:
                    technologies = task.technologies_ids
                else:
                    technologies = technologies + task.technologies_ids

            history.used_technologies = technologies
