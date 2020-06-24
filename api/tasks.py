from background_task import background

from .models import Post


@background(schedule=10)
def reset_post_upvotes():
    posts = Post.objects.all()
    for post in posts:
        post.amount_of_upvotes = 0
        post.save()
