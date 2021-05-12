from django.shortcuts import render


def index(request):
    chat_list = [1, 2, 3]
    context = {'chat_list': chat_list}
    return render(request, 'index.html', context)