# -*- coding: utf-8 -*-
from odoo import fields, models
from datetime import time, datetime, timedelta
from dateutil.relativedelta import relativedelta

class registro_ideas(models.Model):
	_name = "registro.ideas"
	_description = "Tabla de ideas"
	
	name = fields.Char('Nombre de idea', size=256, required=True) 
	codigo = fields.Integer('código', size=20, required=True)
	grupo = fields.Char('Grupo', size=100, required=True)
	descripcion = fields.Char('Descripcion', size=200, required=True)
	fechainicial = fields.Datetime('Fecha Inicial', size=20, required=True)
	fechafinal = fields.Datetime('Fecha Final', required=True, compute='set_calculo_fecha')
	
	@api.depends('fechainicial')
	def set_calculo_fecha(self):
		for rec in self:
			if rec.fechainicial:
				rec.fechafinal = '01/11/2020'
			else:
				rec.fechafinal = '01/11/2021'


	votos = fields.Integer('Votos', size=20, required=True, readonly=True)
	promedio = fields.Float('Promedio',size=10,required=True, readonly=True)






	


