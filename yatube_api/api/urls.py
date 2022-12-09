from rest_framework.routers import SimpleRouter
from django.urls import include, path
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
# from rest_framework.authtoken import views

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
