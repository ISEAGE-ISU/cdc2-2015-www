from django.db import models
from django.contrib.auth.models import User

class SiteUser(models.Model):
  user = models.OneToOneField(User)
  company = models.CharField(default='', max_length=100)

