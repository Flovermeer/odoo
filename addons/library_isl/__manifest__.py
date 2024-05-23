{
    'name' : 'library_ISL',
    'version': '1.0',
    'depends' : ['base'],
    'summaray': "Handle book renting",
    'description': """description""",
    'category': 'Services/Library',
    
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

    'data': [
        'views/library_isl_views.xml',
        'views/library_isl_menuitem.xml',
        'data/a.authormodel.csv',
        'data/a.bookmodel.csv',
        'data/a.commentmodel.csv',
        'data/a.sharehistorymodel.csv',
        'data/a.usermodel.csv',
    ],
}