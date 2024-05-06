from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_product_count = fields.Integer(string="Total Products", compute='_compute_total_product_count')
    customer_email = fields.Char(string="Preferred mail")

    @api.depends('order_line')
    def _compute_total_product_count(self):
        for order in self:
            order.total_product_count = len(order.order_line)
