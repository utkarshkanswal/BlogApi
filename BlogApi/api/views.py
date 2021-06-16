from django.shortcuts import render
from api.models import User, Blog
from rest_framework import viewsets
from api.serializers import UserSerializer, BlogSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
