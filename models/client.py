# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields

class Client(models.Model):
    _name = 'kedamos.client'
    _inherit = 'res.users'

    accountNumber = fields.Integer()
    isPremium = fields.Boolean()
    
    joinEvents = fields.Many2many('kedamos.event')
    myEvents = fields.One2many('kedamos.event', 'organizer')
    myComments = fields.One2many('kedamos.comment', 'user')
