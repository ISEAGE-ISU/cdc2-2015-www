from django.contrib import admin
from cdc.models import SiteUser, LoginSession

admin.site.register(SiteUser)
admin.site.register(LoginSession)
