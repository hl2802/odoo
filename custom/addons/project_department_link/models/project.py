from odoo import models, fields

class ProjectProject(models.Model):
    _inherit = 'project.project'

    department_id = fields.Many2one('hr.department', string='Department')

class HrDepartment(models.Model):
    _inherit = 'hr.department'

    project_ids = fields.One2many('project.project', 'department_id', string='Projects')
