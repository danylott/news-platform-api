from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    link = models.URLField(blank=True, null=True)
    author_name = models.CharField(max_length=100, blank=False, null=False)
    amount_of_upvotes = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    content = models.TextField(null=False, blank=False)
    author_name = models.CharField(max_length=100, blank=False, null=False)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=False, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
