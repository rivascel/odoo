# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    grupo_id = fields.Many2one('registro.grupos','Id Grupo')