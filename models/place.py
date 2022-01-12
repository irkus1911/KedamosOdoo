# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields

class Place(models.Model):
    _name = 'kedamos.place'
    
    name = fields.Char(required=True)
    address = fields.Char(required=True)
    price = fields.Float(digits=(6,2))
    dateRenewal = fields.Date()
    
    event = fields.One2many('kedamos.event', 'place')