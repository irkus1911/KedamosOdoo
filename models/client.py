# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields, api, exceptions 

class Client(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    accountNumber = fields.Integer(required=True)
    isPremium = fields.Boolean(required=True)
    
    joinEvents = fields.Many2many('kedamos.event')
    myEvents = fields.One2many('kedamos.event','organizer')
    myComments = fields.One2many('kedamos.comment','user')

    @api.constrains('accountNumber')
    def _validate_accountNumber(self):
        if self.accountNumber <= 0:
            raise exceptions.ValidationError("Account number cannot be less than zero")
        
    @api.constrains('accountNumber')
    def _validate_accountNumber_lessThanNineDigits(self):
        if len(str(self.accountNumber)) < 9:
            raise exceptions.ValidationError("Account number must have 9 digits")
        
    @api.constrains('accountNumber')
    def _validate_accountNumber_moreThanNineDigits(self):
        if len(str(self.accountNumber)) > 9:
            raise exceptions.ValidationError("Account number must have 9 digits")
    
    @api.onchange('accountNumber')
    def _validate_accountNumberOnChange(self):
        if self.accountNumber < 0:
            raise exceptions.ValidationError("Account number should not be less than zero")