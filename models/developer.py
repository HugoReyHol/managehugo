from odoo import fields, models, api


class developer(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    is_dev = fields.Boolean(default=False)

    technologies_ids = fields.Many2many(
        comodel_name='managehugo.technology',
        string='Technologies',
        relation='developer_technologies',
        column1='developer_id',
        column2='technologies_ids')
