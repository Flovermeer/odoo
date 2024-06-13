{
    'name': 'Library ISL',
    'version': '1.0',
    'summary': 'Module for managing and tracking books in book boxes',
    'description': """
    This module helps in tracking books deposited in book boxes and allows owners to know which user has borrowed their books.
    """,
    'author': 'The Fantastic Three',
    'license' : 'LGPL-3',
    'depends': ['base'],
    'data': [
        'views/book_views.xml',
        'views/user_views.xml',
        'views/book_tracking_views.xml',
        'views/menu_views.xml',
        'security/ir.model.access.csv',
    ],
    
    'application': True,
}