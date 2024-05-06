from odoo import models, fields, tools

class InformeVentes(models.Model):
    _name = 'ventes.sales.report'
    _description = 'Informe de Ventes'
    _auto = False

    user_id = fields.Many2one('res.users', 'Venedor', readonly=True)
    state = fields.Selection([
        ('draft', 'Pressupost'),
        ('sent', 'Pressupost Enviat'),
        ('sale', 'Ordre de Venda'),
        ('done', 'Bloquejat'),
        ('cancel', 'Cancel·lat'),
        ], string='Estat', readonly=True)
    order_count = fields.Integer('Compte dOrdres', readonly=True)
    total_amount = fields.Float('Import Total', readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'ventes_sales_report')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW ventes_sales_report AS (
                SELECT
                    min(so.id) as id,
                    so.user_id as user_id,
                    so.state as state,
                    count(*) as order_count,
                    sum(so.amount_total) as total_amount
                FROM
                    sale_order so
                GROUP BY
                    so.user_id,
                    so.state
            )
        """)
