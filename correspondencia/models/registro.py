from odoo import models, fields, api, exceptions

# def action_print_barCode(self):
#     self.ensure_one()
#     if not self.codeBar_type:
#         raise exceptions.UserError("Debe seleccionar un tipo de documento para generar el código de barras.")
#     if not self.codeBar_type.barcode:
#         raise exceptions.UserError("El tipo de documento seleccionado no tiene un código definido.")
#     return {
#         'type': 'ir.actions.report',
#         'report_name': 'correspondencia.record_tracking_card',
#         'report_type': 'qweb-pdf',
#         'model': self._name,
#         'docsids': [self.id],
#         'context': {
#             'active_model': self._name, 
#             'active_id': self.id,
#             'active_ids': [self.id]
#             },
#     }


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
