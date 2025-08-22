# -*- coding: utf-8 -*-
{
    "name":"correspondencia",
    "summary":"Modelos de Correspondencia",
    'category': 'Correspondencia',
    "description":" Manejo de correspondencia",
    'images': ['static/description/icon.png'],
    "version":"1.0.0",
    "author":"Ivan Rivas", 
    "license":"AGPL-3",
    "depends":["base", "stock", "stock_barcode", "account", 'product'],
    "data":[
        "views/register.xml",
        "security/modulo_security.xml",
        "security/ir.model.access.csv",
        "reports/report.xml",
        "reports/tracking_card.xml"
    ],
    
    "application":True,
    'installable': True,
    'auto_install': False
}