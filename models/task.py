import datetime
from odoo import models, fields, api


class task(models.Model):
    _name = 'managehugo.task'
    _description = 'managehugo.task'

    name = fields.Char(string='Nombre')
    description = fields.Char(string='Descripción')
    start_date = fields.Datetime(string="Fecha comienzo")
    end_date = fields.Datetime(string="Fecha final")
    code = fields.Char(string='Código', compute='_get_code')
    definition_date = fields.Datetime(string="Definición de la tarea", default=lambda _: datetime.datetime.now())
    status = fields.Selection(
        string='Estado',
        selection=[
            ('pendiente', 'Pendiente'),
            ('pausada', 'Pausada'),
            ('en_proceso', 'En proceso'),
            ('completada', 'Completada')
        ],
        group_expand='_expand_groups',
        default='pendiente',
        required=True
    )
        

    # Relaciones entre tablas
    sprint_id = fields.Many2one(comodel_name="managehugo.sprint", string="Sprint", compute="_get_sprint", store=True)
    technologies_ids = fields.Many2many(comodel_name='managehugo.technology',
                                        string='Technologies',
                                        relation='tasks_technologies',
                                        column1="technologies_ids",
                                        column2="tasks_ids")

    history_id = fields.Many2one(
        comodel_name='managehugo.history',
        string='History',
        required=False)

    project_id = fields.Many2one(
        comodel_name='managehugo.project',
        string='Proyecto',
        related="history_id.project_id",
        readonly=True)

    # CAMPOS COMPUTADOS
    def _get_code(self):
        for task in self:
            task.code = "TSK_" + str(task.id)

    @api.depends('code')
    def _get_sprint(self):
        for task in self:
            sprints = self.env['managehugo.sprint'].search([('project_id.id', '=', task.history_id.project_id.id)])
            found = False
            for sprint in sprints:
                if isinstance(sprint.end_date, datetime.datetime) and sprint.end_date > datetime.datetime.now():
                    task.sprint_id = sprint.id
                    found = True
            if not found:
                task.sprint_id = False

    @api.model
    def _expand_groups(self, states, domain, order):
        return ['pendiente', 'pausada', 'en_proceso', 'completada']
