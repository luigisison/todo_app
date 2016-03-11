# -*- coding: utf-8 -*-

{
    'name': 'To-Do Application',    
    'description': 'Manage your personal Tasks with this module.',    
    'author': 'Daniel Reis',    
    'depends': ['mail'],    
    'application': True,
    'summary': 'Luigi's first app',
    'license': 'Affero GPL-3',
    'version': '8.0.1.0',
    'category': 'Extra Tools',
    'data': [
        'todo_view.xml',
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
    ],
} 
