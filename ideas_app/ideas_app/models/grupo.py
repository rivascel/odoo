# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class groupsUsers(models.Model):
    _name = 'groups.users'
    #_inherit = 'res.partner'
    
    id_usuario = fields.Many2one('res.partner','usuario')
    grupo_ids = fields.Many2one('registro.grupos', string='Id Grupo', readonly=True)