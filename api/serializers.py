from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'author_name', 'amount_of_upvotes', 'creation_date')
        read_only_fields = ('amount_of_upvotes', 'creation_date')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author_name', 'post', 'content', 'creation_date')
        read_only_fields = ('creation_date', 'post')
