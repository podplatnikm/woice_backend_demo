from django.conf import settings
from django.contrib import admin

site = "Woice Admin Panel v" + settings.APP_VERSION
admin.site.site_header = site
admin.site.site_title = site
admin.site.index_title = "Admin Panel"
