# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    grupo_ids = fields.Many2one('registro.grupos')

    grupo = fields.Many2one('registro.grupos', 'Grupo',size=100)