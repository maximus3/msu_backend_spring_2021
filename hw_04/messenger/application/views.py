from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods

def index(request):
    chat_list = [1, 2, 3]
    context = {'chat_list': chat_list}
    return render(request, 'index.html', context)