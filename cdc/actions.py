from models import LoginSession, SiteUser
import os
from os import listdir
from os.path import isfile, join
from django.contrib.auth.models import User

def handle_uploaded_file(f, title, user):
  targetdir = 'uploads/' + user.__str__() + '/incoming/'
  if not os.path.exists(targetdir):
    os.makedirs(targetdir)
  with open(targetdir + title, 'wb+') as destination:
    for chunk in f.chunks():
      destination.write(chunk)

def is_logged_in(request):
  return LoginSession.objects.filter(token=request.COOKIES.get('secret_token', False)).exists()

def get_user(request):
  if is_logged_in(request):
    session = LoginSession.objects.get(token=request.COOKIES.get('secret_token', False))
    return SiteUser.objects.get(user=User.objects.get(username=session.user)).user

def list_files(request):
  return None
