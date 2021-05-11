from django.urls import path
from chats.views import chat_list, chat_detail, chat_create

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('<chat_id>/', chat_detail, name='chat_detail'),
    path('new_chat/<chat_id>/', chat_create, name='chat_create'),
]