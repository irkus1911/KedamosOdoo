# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields

class Comment(models.Model):
    _name = 'kedamos.comment'
    
    description = fields.Char(required=True)
    date = fields.Date(required=True)
    mark = fields.Selection([('1', 'ONE'),
                            ('2', 'TWO'),
                            ('3', 'THREE'),
                            ('4', 'FOUR'),
                            ('5', 'FIVE')])
                            
    user = fields.Many2one('res.users', ondelete='set null', string='User', index=True)
    event = fields.Many2one('kedamos.event', ondelete='set null', string='Event', index=True)
