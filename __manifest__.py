# -*- coding: utf-8 -*-
{
    'name': "kedamos",

    'summary': """
       Module to manage all kinds of events
    """,

    'description': """
        This module creates all kinds of events so that each client can manage 
        it. In addition, to be able to join the events created
    """,

    'author': "Kedamos Company",
    'website': "http://www.kedamos.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/client_view.xml',
        'views/templates.xml',
        'views/place_view.xml',
        'views/personal_resource_view.xml',
        'views/personalResource_report.xml',
        'views/event_view.xml',
        'views/client_report.xml',
        'views/event_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}