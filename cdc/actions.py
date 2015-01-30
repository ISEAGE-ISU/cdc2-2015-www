from models import LoginSession

def handle_uploaded_file(f, title):
    with open('uploads/' + title, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def is_logged_in(request):
  return LoginSession.objects.filter(token=request.COOKIES.get('secret_token', False)).exists()
