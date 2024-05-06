from odoo import fields, models


class ModuleReport(models.Model):
    _name = 'module.report'
    _description = "Module Report"
    _rec_name = 'module_field'
    _auto = False