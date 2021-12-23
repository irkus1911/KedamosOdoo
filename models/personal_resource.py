# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields

class personal_resource(models.Model):
    _name='kedamos.personal_resource'
    
    dateExpired=fields.Date()
    dateHired=fields.Date()
    price=fields.Float()
    quantity=fields.Integer()
    personalResource_type=fields.Selection([(1,'CAMARERO'),
                                                 (2,'SEGURIDAD'),
                                                 (3,'DJ'),
                                                 (4,'PAYASO'),
                                                 (5,'MAGO'),
                                                 (6,'HUMOSRISTA'),
                                                 (7,'COCINERO'),
                                                 (8,'GUIA'),
                                                 (9,'ARBITRO'),
                                                 (10,'COCTELERO'),
                                                 (11,'CANTANTE'),
                                                 (12,'MUSICO'),
                                                 (13,'ACTOR')])
                                                 
    event=fields.Many2one('kedamos.event',ondelete='set null', string="Event", index=True)
