# -*- coding: utf-8 -*-
from odoo import models, fields, api 
from datetime import time, datetime, timedelta
from dateutil.relativedelta import relativedelta

class registro_ideas(models.Model):
	_name = "registro.ideas"
	_description = "Tabla de ideas"
	
	name = fields.Char('Nombre de idea', size=256, required=True) 
	codigo = fields.Integer('código', size=20, required=True)
	grupo = fields.Char('Grupo', size=100)
	descripcion = fields.Char('Descripcion', size=200)
	fechainicial = fields.Datetime('Fecha Inicial', size=20, required=True)
	
	@api.depends('fechainicial')
	def _set_calculo_fecha(self):
		for rec in self:
			rec.fechafinal = rec.fechainicial+timedelta(days=30)
			
	fechafinal = fields.Datetime('Fecha Final', compute='_set_calculo_fecha')
	votos = fields.Integer('Votos', size=20, readonly=True, compute='_calc_voto')
	promedio = fields.Float('Promedio',size=10, readonly=True)

	#sumar por cada idea las calificaciones obtenidas y promediar
	def _calc_voto(self):
		for rec in self.env['califica.ideas'].search([]):
			domain=[
				('name','=',rec.idea_id.id)
					]
			records = self.env['califica.ideas'].search(domain)
			scored = records.mapped('calificacion_id')
			rec.average=sum(scored)/len(rec)



    		
    				
    		






	


