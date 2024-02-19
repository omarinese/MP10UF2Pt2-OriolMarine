from odoo import models, fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Model per estate.property.offer"
    price = fields.Float('Preu')
    status = fields.Selection([('Accepted', 'Acceptada'), ('Refused','Descartada')],copy=False)
    partner_id = fields.Many2one('res.partner', string='Comprador',required=True)
    property_id = fields.Many2one('estate.property',string='Propietat',required=True)
    