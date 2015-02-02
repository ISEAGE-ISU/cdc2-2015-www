from django.shortcuts import render, render_to_response, redirect
from models import SiteUser, LoginSession
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from .actions import *

def index(request):
  if request.GET.get('logout', False):
    context = { 'script' : 'True' }
    return render(request, 'cdc/index.html', context)
  return render(request, 'cdc/index.html')

def login(request):
  if is_logged_in(request):
    return HttpResponseRedirect('home')
  elif request.POST.get('next', False) and (not request.POST.get('account', False) or not request.POST.get('company', False) or not request.POST.get('pin', False)):
    context = { 'error' : "Please fill out all fields before submitting." }
    return render(request, 'cdc/login.html', context)
  elif request.POST.get('account', False) and request.POST.get('company', False) and request.POST.get('pin', False):
    # Authentication
    account = request.POST['account']
    company = request.POST['company']
    pin = request.POST['pin']
    # Make sure all POST variables are present
    if account and company and pin:
      if User.objects.filter(username=account).exists():
        siteuser = SiteUser.objects.get(company=company, user=User.objects.get(username=account))
        # if the user supplied the correct password
        if siteuser.user.check_password(pin):
          try:
            token = (LoginSession.objects.all().order_by('pk').reverse()[0].pk + 19) * 14123
          except IndexError:
            token = 19 * 14123
          session = LoginSession(token=token, user=siteuser.user.username)
          session.save()
          response = HttpResponseRedirect('home')
          response.set_cookie('secret_token', token)
          return response
        else:
          context = { 'error' : "The username/password combination you entered doesn't match." }
          return render(request, 'cdc/login.html', context)
      else:
          context = { 'error' : "The user you requested was not found." }
          return render(request, 'cdc/login.html', context)
  else:
    return render(request, 'cdc/login.html')

def logout(request):
  response = redirect('../?logout=true')
  response.delete_cookie('secret_token')
  return response

def account_home(request):
  if is_logged_in(request):
    user = get_user(request)
    page = request.GET.get('page', False)
    context = { 'user' : user.siteuser.company, 'page' : page }
    return render(request, 'cdc/account.html', context)
  return HttpResponseRedirect('cdc:login')

def upload(request):
  user = get_user(request)
  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      handle_uploaded_file(request.FILES['file'], request.POST['title'], user)
      return HttpResponseRedirect('success')
  else:
    form = UploadFileForm()
  return render_to_response('cdc/upload.html', {'form': form})

def success(request):
  return render(request, 'cdc/success.html')

def filings(request):
  user = get_user(request)
  files = list_files(user, '/incoming/')
  return render(request, 'cdc/files.html', { 'files' : files, 'user' : user, 'mode' : 'incoming' })

def reports(request):
  user = get_user(request)
  files = list_files(user, '/outgoing/')
  return render(request, 'cdc/files.html', { 'files' : files, 'user' : user, 'mode' : 'outgoing' })

def warnings(request):
  return None
