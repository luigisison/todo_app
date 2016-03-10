# -*- coding: utf-8 -*

<!-- api enables business logic for the buttons -->
from openerp import models, fields, api 
class TodoTask(models.Model):    
    _name = 'todo.task'    
    name = fields.Char('Description', required=True)    
    is_done = fields.Boolean('Done?')    
    active = fields.Boolean('Active?', default=True)
    
    <!-- Define logic for the Toggle Done button -->
    @api.one
    def do_toggle_done(self):
        self.is_done = not self.is_done
        return True
