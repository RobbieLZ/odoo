# from typing_extensions import Required
from odoo import models, fields


# class EmployeeProfile(models.Model):
#     _name = 'employee.profile'
    
#     name = fields.Char(string="Name")
#     age = fields.Integer("Age")
#     description = fields.Text(string="Description")


class EmployeeProfiles(models.Model):
    _name = 'employee.profile'
    
    name = fields.Char(string="Name", required=True)
    x_email = fields.Char(string="Email")
    
    id = fields.Integer("ID")
    age = fields.Integer("Age", required=True)
    description = fields.Text(string="Description", required=True)