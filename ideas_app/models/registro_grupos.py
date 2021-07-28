# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class registro_grupos(models.Model):
    _name = 'registro.grupos'
    _description = "Tabla de grupos"

    codigo = fields.Integer('Código grupo', size=20, required=True)
    name= fields.Char('Nombre Grupo', size=256, required=True)
    personas_ids = fields.One2many('res.partner','grupo_id','Personas Grupo')

    _sql_constraints = [
                     ('codigo', 
                      'unique(codigo)',
                      'Choose another value - it has to be unique!')]

