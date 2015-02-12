from models import LoginSession, SiteUser
import os
from os import listdir
from django.contrib.auth.models import User

def handle_uploaded_file(f, title, user):
  targetdir = 'uploads/' + user.__str__() + '/incoming/'
  if not os.path.exists(targetdir):
    os.makedirs(targetdir)
  with open(targetdir + title, 'wb+') as destination:
    for chunk in f.chunks():
      destination.write(chunk)

def is_logged_in(request):
  return LoginSession.objects.filter(token=request.COOKIES.get('secret_token', False)).exists() and LoginSession.objects.filter(token=request.COOKIES.get('secret_token', False)).exists()

def is_admin(request):
  return get_user(request).user.is_superuser

def get_user(request):
  if is_logged_in(request):
    session = LoginSession.objects.get(token=request.COOKIES.get('secret_token', False))
    return SiteUser.objects.get(user=User.objects.get(username=session.user)).user

def list_files(account, mode):
  targetdir = 'uploads/' + account.__str__() + mode
  if os.path.exists(targetdir):
    return [ f for f in listdir(targetdir) ]
  else:
    return False

def create_session(user):
  try:
    # Generate a very secret session token for the user
    token = (LoginSession.objects.all().order_by('pk').reverse()[0].pk + 19) * 14123
  # Bad things can happen if this is the first session
  except IndexError:
    token = 19 * 14123
  session = LoginSession(token=token, user=user)
  session.save()
  return token
