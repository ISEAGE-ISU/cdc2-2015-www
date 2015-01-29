from django.shortcuts import render
from models import SiteUser
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
  return render(request, 'cdc/index.html')

def login(request):
  if request.user.is_authenticated():
    return render(request, 'cdc/index.html')
  if request.POST.get('account', False) and request.POST.get('company', False) and request.POST.get('pin', False):
    # Authentication
    account = request.POST['account']
    company = request.POST['company']
    pin = request.POST['pin']
    # Make sure all POST variables are present
    if account and company and pin:
      if User.objects.filter(username=account).exists():
        siteuser = SiteUser.objects.get(company=company, user=User.objects.get(username=account))
        # if the user exists and supplied the correct password
        if siteuser and siteuser.user.check_password(pin):
          return render(request, 'cdc/account.html')
        else:
          context = { 'error' : "The username/password combination you entered doesn't match." }
          return render(request, 'cdc/account.html', context)
      else:
          context = { 'error' : "The user you requested was not found." }
          return render(request, 'cdc/account.html', context)
    else:
      context = { 'error' : "Please fill out all fields before submitting." }
      return render(request, 'cdc/account.html', context)
    return render(request, 'cdc/login.html')

  return render(request, 'cdc/login.html')
# return redirect('/login/?next=%s' % request.path)

def logout(request):
  logout(request)
  return render(request, 'cdc/index.html')

def account_home(request):
  return render(request, 'cdc/account.html')

