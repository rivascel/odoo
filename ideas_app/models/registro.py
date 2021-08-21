# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from datetime import date, time, datetime, timedelta
from dateutil.relativedelta import relativedelta


class registro_ideas(models.Model):
    _name = "registro.ideas"
    _description = "Tabla de ideas"

    name = fields.Char('Nombre de idea', size=256, required=True)
    codigo_grupo = fields.Many2one('registro.grupos', 'codigo grupo', size=20, required=True)
    grupo = fields.Many2one('registro.grupos', 'Grupo',size=100)
    codigo = fields.Integer(string='codigo idea', size=20, required=True)    
    descripcion = fields.Char('Descripcion', size=200)
    fechainicial = fields.Datetime('Fecha Inicial', size=20, required=True, default=date.today().strftime('%Y-%m-%d'))
    usuario_id= fields.Many2one('res.users', 'Usuario', readonly=True, default=lambda self: self.env.user)


    @api.depends('fechainicial')
    def _set_calculo_fecha(self):
        for rec in self:
            rec.fechafinal = rec.fechainicial+timedelta(days=30)

    fechafinal = fields.Datetime('Fecha Final', compute='_set_calculo_fecha')
    promedio = fields.Float('Promedio', size=10, readonly=True, compute='_calc_voto')
    promedioUsu = fields.Float('Promedio Usuario', size=10, readonly=True, compute='_calc_voto_usu')


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
        
    def _calc_voto_usu(self):
        for rec in self:
            average_scored=0
            scored_ids=self.env['califica.ideas'].search([('usuario_id','=',rec.usuario_id.id)])
            if scored_ids:
                number = len(scored_ids)
                for scored in scored_ids:
                    average_scored += scored.calificacion_id/number
        rec.promedioUsu = average_scored

