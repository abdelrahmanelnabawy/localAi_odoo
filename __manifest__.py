{
    'name': "kti_localAi",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [        
        'base',
        'web',
        'mail',
    ],

    'data': [
        'security/ir.model.access.csv',
        'security/llm_security_rules.xml',
        'views/llm_config_views.xml',
        'views/llm_conversation_views.xml',
        'views/llm_menu_views.xml',
        'data/llm_config_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'kti_local_ai/static/src/js/llm_chat_widget.js',
            'kti_local_ai/static/src/xml/llm_chat_templates.xml',
            'kti_local_ai/static/src/css/llm_chat.css',
        ],
    },
    'images': [
        'static/description/banner.png',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

