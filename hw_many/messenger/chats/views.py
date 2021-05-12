from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def chat_list(request):
    print(reverse('chat_list'))
    return JsonResponse({'chat_list': [1, 2, 3]})


@require_http_methods(["GET"])
def chat_detail(request, chat_id):
    print(reverse('chat_detail', kwargs={'chat_id': chat_id}))
    return JsonResponse({'status': 'ok', 'chat_id': chat_id})


@require_http_methods(["POST"])
def chat_create(request, chat_id):
    print(reverse('chat_create', kwargs={'chat_id': chat_id}))
    return JsonResponse({'status': 'ok', 'chat_id': chat_id})