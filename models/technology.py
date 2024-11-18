from odoo import fields, models, api


class technology(models.Model):
    _name = 'managehugo.technology'
    _description = 'managehugo.technology'

    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
    photo = fields.Image(string='Foto')

    # Relaciones entre tablas
    tasks_ids = fields.Many2many(comodel_name='managehugo.task',
                                 string='Tasks',
                                 relation='tasks_technologies',
                                 column1="tasks_ids",
                                 column2="technologies_ids")
