{
    'name': 'Custom Theme Color',
    'version': '1.0',
    'category': 'Customization',
    'summary': 'Customize theme color',
    'description': 'This module allows users to customize the theme color.',
    'author': 'Nguyen Huong IT',
    'depends': ['web', 'base'],
    'data': [
        'views/assets.xml',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_theme_color/static/src/css/custom_theme.css',
            'custom_theme_color/static/src/js/custom_theme.js',
        ],
    },
    'installable': True,
    'application': False,
}
