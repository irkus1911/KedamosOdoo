# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields

class User(models.Model):
    
    _name = 'res.users'
    _inherit = 'res.users'
    
    fullName = fields.Char()
    status = fields.Selection(('user', 'USER'),('admin','ADMIN'))
    lastPasswordChange = fields.DateTime()
    email = fields.Char()
    username = fields.Char()
    password = fields.Char()
    privilege = fields.Selection(('enabled','ENABLED'),('disabled','DISABLED'))
    
    
