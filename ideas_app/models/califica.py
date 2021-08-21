# -*- coding: utf-8 -*-
from odoo import fields, models,api, exceptions
from types import *
from datetime import datetime, time

class califica_ideas (models.Model):   
	_name = "califica.ideas"

	name = fields.Many2one('registro.ideas','Idea')
	codigo = fields.Integer(string='codigo', related='name.codigo', store=True)
	calificacion_id = fields.Float('calificacion', size=10, required=True)
	fecha_actual = fields.Datetime('Fecha Calificacion', default=datetime.now(), readonly=True)
	usuario_id= fields.Many2one('res.users', 'Usuario', readonly=True, default=lambda self: self.env.user)
	promedioUsu = fields.Float('Promedio Usuario', size=10, readonly=True, compute='_calc_voto_usu')

	@api.constrains('calificacion_id')
	def _calif(self):
		for record in self:
			if (record.calificacion_id < 0) or (record.calificacion_id > 10):
				raise exceptions.ValidationError('La calificación debe ser entre 0 y 10')
	
	#Se genene una restriccion para que el usuario solo puede calificar una sola vez una Idea 
	@api.constrains('codigo','usuario_id')
	def _validaVoto(self):
		for data in self:
			domain=[
					('codigo','=',self.codigo),
					('usuario_id','=',self.create_uid.id)
					]
			records=self.search(domain)
			codigo_ids=records.mapped('calificacion_id')
			data.total1 = len(codigo_ids)

			if data.total1 > 1:
				raise exceptions.ValidationError('Ya califico esta idea')	

	