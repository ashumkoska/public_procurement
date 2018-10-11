{
    'name': 'Public Procurement',
    'version': '11.0.1.0.0',
    'author': 'Aleksandra Shumkoska', 
    'support': 'a_shumkoska@yahoo.com',
    'license': 'Other proprietary',
    'category': 'Purchases',
    'summary': 'Public Procurement',
    'description': ''' 
        Public Procurement 
    ''',
    'depends': [
        'mail', 
        'purchase',
        'web_digital_sign'
    ],
    'data': [
        'views/procurement_offer.xml',
        'views/procurement_plan.xml',
        'views/mail_activity.xml',
        'views/menu.xml'
    ],
    'installable': True,
    'auto_install': False,
    'price': 00.00,
    'currency': 'EUR',
}
