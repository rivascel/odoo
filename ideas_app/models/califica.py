# -*- coding: utf-8 -*-
from odoo import fields, models,api, exceptions
from types import *
from datetime import datetime, time

class califica_ideas (models.Model):   
	_name = "califica.ideas"
	#__inherit = 'registro'

	idea_id = fields.Many2one('registro.ideas','codigo')
	calificacion_id = fields.Float('calificacion', size=10, required=True)
	fecha_actual = fields.Datetime('Fecha Calificacion', default=datetime.now(), readonly=True)
	usuario_id= fields.Many2one('res.partner', 'id usuario', required=True)
	
	@api.constrains('calificacion_id')
	def _calif(self):
		for record in self:
			if (record.calificacion_id < 0) or (record.calificacion_id > 10):
				raise exceptions.ValidationError('La calificación debe ser entre 0 y 10')
				




