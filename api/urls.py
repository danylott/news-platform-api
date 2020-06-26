from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from .views import PostViewSet, CommentViewSet, overview, task


router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("task/", task),
    path("overview/", overview),
]
