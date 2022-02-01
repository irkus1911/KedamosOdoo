# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields

class EventManager(models.Model):
    _inherit = 'res.users'
        
    managerCategory = fields.Selection([('ocio','OCIO'),
                                       ('deportes','DEPORTES'),
                                       ('fiesta','FIESTA'),
                                       ('cultura','CULTURA'),
                                       ('excursiones','EXCURSIONES'),
                                       ('videojuegos','VIDEOJUEGOS'),
                                       ('juegos_de_mesa','JUEGOS_DE_MESA'),
                                       ('musica','MUSICA'),
                                       ('otros','OTROS')])
                                       
    myRevisions = fields.One2many('kedamos.revise', 'user')