# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields

class Event(models.Model):
    _name= 'kedamos.event'
    
    date=fields.Date(required=True)
    maxParticipants=fields.Integer(required=True)
    minParticipants=fields.Integer(required=True)
    actualParticipants=fields.Integer(required=True)
    description=fields.Char()
    price=fields.Float()
    isRevised=fields.Boolean(required=True)
    title=fields.Char(required=True)
    event_category=fields.Selection([(1, 'OCIO'),
                                     (2, 'DEPORTES'),
                                     (3, 'FIESTA'),   
                                     (4, 'CULTURA'),
                                     (5, 'EXCURSIONES'),
                                     (6, 'VIDEOJUEGOS'),
                                     (7, 'JUEGOS_DE_MESA'),
                                     (8, 'MUSICA'),
                                     (9, 'OTROS')])
                                     
    personal=fields.One2many('kedamos.personal_resource', 'event')
    organizer=fields.Many2one('kedamos.client')
    place=fields.Many2one('kedamos.place')
    comment=fields.One2many('kedamos.comment', 'event')
    participants=fields.Many2many('kedamos.client')
    eventRevisions=fields.One2many('kedamos.revise', 'event')