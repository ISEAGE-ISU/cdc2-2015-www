from django.contrib import admin
from cdc.models import SiteUser, LoginSession, Testimonial

admin.site.register(SiteUser)
admin.site.register(LoginSession)
admin.site.register(Testimonial)
