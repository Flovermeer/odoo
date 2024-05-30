# -*- coding: utf-8 -*-
{
    'name': "library",

    'summary': "Application de gestion de location de livres",

    'description': """
Cette application permet de gérer la location de livres et de faire leur suivi.
    """,

    'author': "Arthur - Guillaume - Florence",
    'website': "http://www.odoo.com",
    
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/library_security.xml',
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

