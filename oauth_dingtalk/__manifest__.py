# -*- coding: utf-8 -*-
###################################################################################
#    Copyright (C) 2020 PaulLu LGPL-3
###################################################################################
{
    'name': "钉钉扫码登录",
    'summary': """不需要在Odoo系统中绑定钉钉uid，可使用员工的手机号码比对一致后登录""",
    'description': """不需要在Odoo系统中绑定钉钉uid，可使用员工的手机号码比对一致后登录""",
    'author': "Paul Lu",
    'website': "https://www.odoo.live",
    'category': 'dingtalk',
    'version': '1.0',
    'depends': ['auth_oauth', 'hr'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'data/auth_oauth_data.xml',
        'views/res_config_settings_view.xml',
        'views/login_templates.xml',
    ],
    'license': 'LGPL-3',
    'support': 'luss613@gmail.com',
    'images': ['static/description/login_page.png']
}
