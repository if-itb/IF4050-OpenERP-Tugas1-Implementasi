# -*- coding: utf-8 -*-
{
    'name': "Personal Expense",

    'summary': """Managing User Personal Expense""",

    'description': """This module is used to help user in managing their daily personal expense""",

    'author': "Christian Hendy",
    'website': "http://www.christianhendy.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Manager',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
