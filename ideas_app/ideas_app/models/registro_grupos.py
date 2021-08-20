# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class registro_grupos(models.Model):
    _name = 'registro.grupos'
    _description = "Tabla de grupos"

    codigo = fields.Integer('Código grupo', required=True)
    name= fields.Char('Nombre Grupo', required=True)
    
    personas_gr = fields.One2many('groups.users','grupo_ids','Personas Grupo')

    _sql_constraints = [
                     ('codigo', 
                      'unique(codigo)',
                      'Choose another value - it has to be unique!')]

