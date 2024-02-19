from odoo import models, fields, api
from datetime import timedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Propietats Immobiliàries'

    name = fields.Char('Nom', required=True)
    description = fields.Text('Descripció')
    postcode = fields.Char('Codi Postal', required=True)
    expected_selling_price = fields.Float('Preu esperat', digits=(12, 2), currency_field='currency_id', default=0.0)
    elevator = fields.Boolean('Ascensor', default=False)
    date_availability = fields.Date('Data disponibilitat', copy=False, default=lambda self: (fields.Date.today() + timedelta(days=30)))
    parking = fields.Boolean('Aparcament', default=False)
    renovated = fields.Boolean('Renovat', default=False)
    bathroom = fields.Integer('Numero de banys')
    area = fields.Integer('Superfície', required=True)
    selling_price = fields.Monetary('Preu venda', currency_field='currency_id')
    best_offer = fields.Monetary('Millor oferta', currency_field='currency_id',compute='_compute_best_offer', store=True, readonly=True)
    bedrooms = fields.Integer('Nombre habitacions', required=True)
    energy_certificate = fields.Char('Certificat energetic', size=1)
    buyer_id = fields.Many2one('res.partner', string='Comprador')
    salesperson_id = fields.Many2one('res.users', string='Comercial', default=lambda self: self.env.user.id)
    currency_id = fields.Many2one('res.currency', string='Moneda', default=lambda self: self.env.company.currency_id)
    state = fields.Selection([('New', 'Nou'),('Offer Received', 'Oferta Rebuda'),('Offer Accepted', 'Oferta Acceptada'),('Sold', 'Venuda'),('Canceled', 'Cancel·lada')], default='New', copy=False, required=True)
    active = fields.Boolean('Actiu', default=False, invisible=True)
    avgPrice = fields.Float('Preu per m2',compute='_calcular_preu_per_metre')
    construction_year = fields.Integer('Any de construcció')
    tag_ids = fields.Many2many('estate.property.tag', string='Etiquetes')
    offer_ids = fields.One2many('estate.property.offer','property_id', string='Ofertes')
    type_id = fields.Many2one('estate.property.types', string='Tipus')




    @api.depends('expected_selling_price','area')
    def _calcular_preu_per_metre(self):
        for record in self:
            if record.area > 0 :
                record.avgPrice = record.expected_selling_price/record.area
            else:
                record.avgPrice = None

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for property_record in self:
            best_price = 0.0
            for offer in property_record.offer_ids:
                if offer.price > best_price:
                    best_price = offer.price
            property_record.best_offer = best_price