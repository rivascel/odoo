# -*- coding: utf-8 -*-
from odoo import fields, models
from types import *
from datetime import datetime, time

class califica_ideas (models.Model):   
	_name = "califica.ideas"
	__inherit = 'registro'

	idea_id = fields.Many2one('registro.ideas','codigo')
	calificacion_id = fields.Float('calificacion', size=10, required=True)
	fecha_actual = fields.Datetime('Fecha Calificacion', default=datetime.now(), required=True, readonly=True)
	usuario_id= fields.Many2one('res.partner', 'id usuario', required=True)
	votos = fields.Integer('Votos', size=20, required=True, readonly=False)
	promedio = fields.Float('Promedio',size=10,required=True, readonly=False)


