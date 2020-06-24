from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['POST'])
    def upvote(self, request, pk=None):
        try:
            post = Post.objects.get(id=pk)
            post.amount_of_upvotes = post.amount_of_upvotes + 1
            post.save()
            serializer = PostSerializer(post)
            response = {'message': 'You have successfully upvoted this post!', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            response = {'message': 'Such post does not exist!'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def comment(self, request, pk=None):
        if 'content' in request.data and 'author_name' in request.data:
            try:
                post = Post.objects.get(id=pk)
                content = request.data['content']
                author_name = request.data['author_name']

                comment = Comment.objects.create(post=post, content=content, author_name=author_name)
                serializer = CommentSerializer(comment)
                response = {'message': 'Comment successfully created', 'result': serializer.data}
                return Response(response, status.HTTP_201_CREATED)

            except ObjectDoesNotExist:
                response = {'message': 'Such post does not exist!'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

        else:
            response = {'message': 'You need to provide content and author_name'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create comment like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
