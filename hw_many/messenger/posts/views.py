from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets

from posts.models import Post
from posts.forms import PostForm
from posts.serializers import PostSerializer

from posts.tasks import send_email_if_new_object

from posts.documents import PostDocument


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


@login_required
@require_http_methods(["GET"])
def post_search(request):
    searched_posts = PostDocument.search().query("match", title=request.GET['title'])

    context = {'post_list': searched_posts}
    return render(request, 'posts.html', context)


@login_required
@require_http_methods(["GET"])
def post_my(request):
    context = {'post_list': [post for post in Post.objects.filter(author_id=request.user.id)]}
    return render(request, 'posts_my.html', context)

@login_required
@require_http_methods(["GET"])
def post_list(request):
    context = {'post_list': [post for post in Post.objects.all()]}
    return render(request, 'posts.html', context)


@login_required
@require_http_methods(["GET"])
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'post_detail.html', context)


@login_required
@require_http_methods(["POST"])
def post_create(request):
    author = request.user  # User.objects.get(username='anonymous')
    my_post = dict(request.POST)
    my_post.update({'author': author})
    form = PostForm(my_post)
    if form.is_valid():
        post = form.save()
        context = {'post_list': [post for post in Post.objects.all()]}
        send_email_if_new_object.delay(post.title)
        return render(request, 'posts.html', context)
    return JsonResponse({'errors': form.errors}, status=400)


@login_required
@require_http_methods(["PUT"])
def post_update(request, post_id, new_text):
    post = get_object_or_404(Post, pk=post_id)
    post.text = new_text
    post.save()
    return JsonResponse({'status': 'ok'})


@login_required
@require_http_methods(["DELETE"])
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return JsonResponse({'status': 'ok'})