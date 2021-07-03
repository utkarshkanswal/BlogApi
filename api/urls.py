from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, BlogViewSet


router = DefaultRouter(trailing_slash=False)

router.register('user', UserViewSet, basename='user')
router.register('blog', BlogViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
]
