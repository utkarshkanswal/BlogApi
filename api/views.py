from rest_framework import response
from api.models import User, Blog
from rest_framework import serializers, viewsets
from api.serializers import UserSerializer, BlogSerializer
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        obj = User.objects.all()
        response = UserSerializer(obj, many=True)
        return Response({"data": response.data})

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response({'message': "Some Error Occurred"})

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def create(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response({'message': "Some Error Occurred"})

    def list(self, request, *args, **kwargs):
        obj = Blog.objects.all()
        response = BlogSerializer(obj, many=True)
        return Response({"blog_data": response.data})
