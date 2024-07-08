from odoo import models, fields

class ProjectProject(models.Model):
    _inherit = 'project.project'
    date_end = fields.Date(string="End Date")
    department_id = fields.Many2one('hr.department', string='Phòng Ban')
    responsible_department_id = fields.Many2one('hr.department', string='Phòng Ban Phụ Trách')
    
class HrDepartment(models.Model):
    _inherit = 'hr.department'

    project_ids = fields.One2many('project.project', 'department_id', string='Projects')
