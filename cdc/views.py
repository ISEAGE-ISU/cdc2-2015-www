from django.shortcuts import render


def index(request):
  return render(request, 'cdc/index.html')

def login(request):
  return render(request, 'cdc/index.html')

def logout(request):
  return render(request, 'cdc/index.html')

def account_home(request):
  return render(request, 'cdc/index.html')

