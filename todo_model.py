# -*- coding: utf-8 -*

<!-- api enables business logic for the buttons -->
from openerp import models, fields, api

<!-- todo.task model -->
class TodoTask(models.Model):    
    _name = 'todo.task'    
    name = fields.Char('Description', required=True)    
    is_done = fields.Boolean('Done?')    
    active = fields.Boolean('Active?', default=True)
