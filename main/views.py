import urllib
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
import requests
from .models import PushbulletClient
from .tasks import notification


def check(request):
    notification()
    return redirect('home')

def home(request):
    client_id = settings.PUSHBULLET_CLIENT_ID
    raw_url = ''.join([request.scheme, '://', request.META['HTTP_HOST'], '/register'])
    redirect_uri = urllib.quote_plus(raw_url)
    return render(request, 'main/home.html', locals())

def register(request):
    pushbullet_code = request.GET.get('code', False)
    if pushbullet_code:
        auth_request = {
            'client_id': settings.PUSHBULLET_CLIENT_ID,
            'client_secret': settings.PUSHBULLET_CLIENT_SECRET,
            'code': pushbullet_code,
            'grant_type': 'authorization_code',
        }
        response = requests.post('https://api.pushbullet.com/oauth2/token', data=auth_request)
        if response.status_code == 200:
            response_json = response.json()
            PushbulletClient(access_token=response_json['access_token']).save()
            messages.success(request, 'Cadastro realizado com sucesso!')
        else:
            messages.error(request, 'Erro no cadastro. Tente novamente mais tarde.')
    return redirect('home')
