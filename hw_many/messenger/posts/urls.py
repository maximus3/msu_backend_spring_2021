from django.urls import path, re_path
from posts.views import post_list, post_detail, post_create, post_delete, post_update

urlpatterns = [
    re_path(r'$^', post_list, name='post_list'),
    path('new', post_create, name='post_create'),
    path('update/<post_id>/<new_text>', post_update, name='post_update'),
    path('delete/<post_id>', post_delete, name='post_delete'),
    path('<post_id>', post_detail, name='post_detail'),
]