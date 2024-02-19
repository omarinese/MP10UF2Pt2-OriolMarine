from odoo import models, fields


class EstatePropertyTypes(models.Model):

    
    _name = "estate.property.types"
    _description = "Model per estate.property.types"
    name = fields.Char(string='Tipus', required=True)
    properties_ids = fields.One2many('estate.property', 'type_id', string='Propietats')

    
   
    
    