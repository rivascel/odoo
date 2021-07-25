# -*- coding: utf-8 -*-
from odoo import fields, models,api, exceptions
from types import *
from datetime import datetime, time

class califica_ideas (models.Model):   
	_name = "califica.ideas"
	#__inherit = 'registro'

	name = fields.Many2one('registro.ideas','Idea')
	codigo = fields.Integer(string='codigo', related='name.codigo', store=True)
	calificacion_id = fields.Float('calificacion', size=10, required=True)
	fecha_actual = fields.Datetime('Fecha Calificacion', default=datetime.now(), readonly=True)
	usuario_id= fields.Many2one('res.users', 'Usuario', readonly=True, default=lambda self: self.env.user)
	
	@api.constrains('calificacion_id')
	def _calif(self):
		for record in self:
			if (record.calificacion_id < 0) or (record.calificacion_id > 10):
				raise exceptions.ValidationError('La calificación debe ser entre 0 y 10')
	
	#Se genene una restriccion para que el usuario solo puede calificar una sola vez una Idea 
	@api.constrains('codigo','usuario_id')
	def _validaVoto(self):
		if self.codigo and self.usuario_id:
			codigo_ids = self.search_count([('codigo','=',self.codigo)])
			usuario_ideas_ids = self.search_count([('usuario_id','=',self.create_uid.id)])
			if codigo_ids > 1 and usuario_ideas_ids > 1:
				raise exceptions.ValidationError('Ya califico esta idea')		

	
