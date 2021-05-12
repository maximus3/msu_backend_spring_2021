from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from posts.models import Post
from users.models import User


@require_http_methods(["GET"])
def post_list(request):
    context = {'post_list': [post for post in Post.objects.all()]}
    return render(request, 'posts.html', context)


@require_http_methods(["GET"])
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'post_detail.html', context)


@require_http_methods(["POST"])
def post_create(request):
    if 'title' not in request.POST:
        return JsonResponse({'status': 'error', 'error': 'No title in parameters'})
    title = request.POST['title']
    text = request.POST.get('text')
    text = text or ''
    author = User.objects.get(username='anonymous')
    post = Post(title=title, text=text, author=author)
    post.save()
    context = {'post_list': [post for post in Post.objects.all()]}
    return render(request, 'posts.html', context)


@require_http_methods(["PUT"])
def post_update(request, post_id, new_text):
    post = get_object_or_404(Post, pk=post_id)
    post.text = new_text
    post.save()
    return JsonResponse({'status': 'ok'})


@require_http_methods(["DELETE"])
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return JsonResponse({'status': 'ok'})