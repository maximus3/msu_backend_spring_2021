from celery import shared_task
from posts.models import Post
import time


@shared_task()
def posts_count_celery(filename='posts_count.txt'):
    cnt = Post.objects.count()
    with open(filename, 'a') as f:
        print(f'{time.asctime()}: Posts count - {cnt}', file=f)


@shared_task()
def add(a, b):
    return a + b


@shared_task()
def mul(a, b):
    return a * b


@shared_task()
def xsum(numbers):
    return sum(numbers)