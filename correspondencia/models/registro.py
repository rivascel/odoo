from odoo import models, fields, api, exceptions


class Correspondencia(models.Model):
    _name = "correspondencia.correspondencia"
    _description = "Correspondencia"

    name = fields.Char("Nombre", size=256)
    description = fields.Text("Descripción")
    origin = fields.Many2one("stock.location", string="Dependencia Origen")
    responsible = fields.Many2one("hr.employee", string="Responsable")
    finalLocation = fields.Many2one("stock.location", size=256, string="Dependencia destino")
    destination=fields.Many2one("res.partner", string="Destinatario")
    
    document_type = fields.Selection([
        ('in', "Entrada"),
        ('out', "Salida"),
        ('internal', "Interna"),
    ], default='in')
    codeBar_type = fields.Many2one("product.product", string="Tipo documento")
    barcode = fields.Char('Barcode', index=True)
    date = fields.Date("Fecha", default=fields.Date.today)
    number_sheets=fields.Integer("Número de hojas")
    sender=fields.Many2one("res.partner", string="Remitente")
    name_sender=fields.Text("Nombre del remitente")
    address=fields.Text("Dirección")
    phone=fields.Text("Teléfono")
    attachment=fields.Binary("Adjunto")
    tracking=fields.One2many("stock.picking", "name", string="Rastreo", readonly=True)

    def print_report(self):
       return self.env.ref('correspondencia.action_record_tracking_card').report_action(self)
