from __future__ import unicode_literals

from django.conf import settings


def populate_settings(app_settings, default):
    for key in app_settings.keys():
        if isinstance(app_settings[key], dict) and key in default.keys():
            app_settings[key] = populate_settings(app_settings[key], default[key])
    default.update(app_settings)
    return default

DEFAULT_BLOG_SETTINGS = {
    'ENABLE_CUSTOM_PANEL': False,
    'ADMIN_PANEL_URL': "^admin/",
    'SITE_HEADER': "Blog administration panel",
    'SITE_TITLE': "Blog panel",
    'INDEX_TITLE': "Welcome to Blog admin panel",
    'ADD_META': False
}

APP_SETTINGS = getattr(settings, 'BLOG_SETTINGS', None)
BLOG_SETTINGS = populate_settings(APP_SETTINGS, DEFAULT_BLOG_SETTINGS)
