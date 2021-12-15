# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Revise(models.Model):
    _name = 'kedamos.revise'

    reviseDate = fields.Date(required=True)
    event = fields.Many2One('kedamos.event', ondelete='set null', string='Event', index=True)
    user = fields.Many2One('kedamos.eventManager', ondelete='set null', string='User', index=True)
