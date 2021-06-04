from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect
from application.local_settings import CENTRIFUGE_TOKEN


def login_required(func):
    def wrapped(request, *args, **kwargs):
        if isinstance(request.user, AnonymousUser):
            return redirect('login')
        return func(request, *args, **kwargs)
    return wrapped


def index(request):
    chat_list = [1, 2, 3]
    context = {'chat_list': chat_list}
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html', {'CENTRIFUGE_TOKEN': CENTRIFUGE_TOKEN})