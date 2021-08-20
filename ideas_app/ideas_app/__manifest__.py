# -*- coding: utf-8 -*-

{
    'name': 'MODULO DE REGISTRO Y CALIFICACION DE IDEAS',
    'version': '1.0',
    'author': 'Iván Rivas C.',
    'category': 'Test',
    'depends' : ['base'],
    'data': [
        'views/registro_view.xml',
        'views/califica_view.xml',
        'views/grupo_view.xml',
        'security/security_registro.xml',
        'security/security_califica.xml',
        'security/security_grupo.xml',
        'security/security_usersGroup.xml'
    ],
    'installable': True,
    'active': True,
    'auto_install': False,
    'application': True,
    
}
