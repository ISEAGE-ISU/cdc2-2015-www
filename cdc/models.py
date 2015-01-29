from django.db import models
from django.contrib.auth.models import User

class SiteUser(models.Model):
  # Using a OneToOneField so we can add the extra 'company' parameter to the user
  # without extending or replacing Django's User model
  user = models.OneToOneField(User)
  company = models.CharField(default='', max_length=100)

