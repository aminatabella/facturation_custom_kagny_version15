# -*- coding: utf-8 -*-

{
    'name': 'Système de facturation et Customisation',
    'version': '1.4',
    'author': 'Bella Bah',
    'website': 'https://www.aminatabella.com',
    'support': 'baminatabella@gmail.com',
    'license': "AGPL-3",
    'complexity': 'easy',
    'sequence': 5,
    'category': 'Facturation',
    'description': """
        Système de facturation et Customisation
    """,
    'depends': [
        'base',
        'account',
        'product',
        'mail'
    ],
    'summary': 'summary1, summary2, ',
    'data': [
        #'security/facture_securite.xml',
        #'security/ir.model.access.csv',
        #'data/${ModuleName}_data.xml',
        'views/facture_inherit.xml',
        'reports/report_invoice_inherit.xml',
        #'menu.xml',
    ],
    'demo': [
    	#'demo/${ModuleName}_demo.xml'
    ],
    'css': [
    	#'static/src/css/${ModuleName}_style.css'
    ],

    'price': 0.00,
    'currency': 'EUR',
    'installable': True,
    'application': True,
}