from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet,
    CommentViewSet,
    GroupViewSet,
)

router = DefaultRouter()
router.register(
    r'posts',
    PostViewSet,
)
router.register(
    r'posts/(?P<post_id>[^/.]+)/comments',
    CommentViewSet,
    basename='comments',
)
router.register(
    r'groups',
    GroupViewSet,
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
