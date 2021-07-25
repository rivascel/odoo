# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from datetime import date, time, datetime, timedelta
from dateutil.relativedelta import relativedelta


class registro_ideas(models.Model):
    _name = "registro.ideas"
    _description = "Tabla de ideas"

    name = fields.Char('Nombre de idea', size=256, required=True)
    #codigo = fields.Many2one('registro.grupos', 'codigo', size=20, required=True)

    grupo = fields.Many2one('registro.grupos', 'Grupo',size=100)
    codigo = fields.Integer(string='codigo', related='grupo.codigo', store=True)    
    

    
    descripcion = fields.Char('Descripcion', size=200)
    fechainicial = fields.Datetime('Fecha Inicial', size=20, required=True, default=date.today().strftime('%Y-%m-%d'))

    @api.depends('fechainicial')
    def _set_calculo_fecha(self):
        for rec in self:
            rec.fechafinal = rec.fechainicial+timedelta(days=30)

    fechafinal = fields.Datetime('Fecha Final', compute='_set_calculo_fecha')
    votos = fields.Float('Votos', size=20, readonly=True)
    promedio = fields.Float('Promedio', size=10, readonly=True, compute='_calc_voto')

#    _sql_constraints = [
#                     ('codigo', 
#                      'unique(codigo)',
#                      'Choose another value - it has to be unique!')]

    #suma el campo 'calificacion_id' del modelo 'califica' agrupado por el campo 'codigo'
    def _calc_voto(self):
        for rec in self:
            average_scored=0
            scored_ids=self.env['califica.ideas'].search([('codigo','=',rec.codigo)])
            if scored_ids:
                number = len(scored_ids)
                for scored in scored_ids:
                    average_scored += scored.calificacion_id/number

        rec.promedio = average_scored
        
    

