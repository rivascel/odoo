# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class registro_grupos(models.Model):
    _name = 'registro.grupos'
    _description = "Tabla de grupos"

    name= fields.Char('Nombre Grupo', size=256)
    codigo = fields.Integer('Código grupo', size=20, required=True)
    personas_id = fields.One2many('res.partner','grupo_ids','Personas Grupo')

    _sql_constraints = [
                     ('codigo', 
                      'unique(codigo)',
                      'Choose another value - it has to be unique!')]

