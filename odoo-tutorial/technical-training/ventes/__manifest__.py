{
    "name": "ventes",
    "version": "16.0.0",
    "application": True,
    "depends": ["base", "sale"],
    "data": [
        'security/ir.model.access.csv',
        'views/sale_order_form_inherit.xml',
        'reports/sale_order_report_inherit.xml',
    ],
    "installable": True,
    'license': 'LGPL-3',
}