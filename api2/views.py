# from django.contrib.auth.models import User
# from rest_framework import viewsets
#
# from api2.serializers import UserSerializer, PostSerializer, CommentSerializer
# from blog.models import Post, Comment
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
# ------------------------------------------------
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from api2.serializers import CommentSerializer, PostListSerializer, PostRetrieveSerializer
from blog.models import Post, Comment


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


# PostListAPIView 와 내부 구현은 같지만 서로 다른 클래스를 상속 받기 때문에 다른 동작을 한다
class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
