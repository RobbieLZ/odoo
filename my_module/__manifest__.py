{
    'name': "Employee Record",
    'summary': """Simple employee data""",
    'description': """Simple employee data""",
    'author': "Robbie",
    'website': "http://www.yourcompany.com",
    'category': 'Management',
    'version': '0.1',
 
    'depends': ['base'],

    'data': [
        'views/employee_view.xml',
        'security/ir.model.access.csv'
    ],

    'installable' : True,
    'application' : True,
}
