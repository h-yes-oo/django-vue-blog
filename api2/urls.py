# Routers provide an easy way of automatically determining the URL conf.
# from django.urls import path, include
# from rest_framework import routers
#
# from api2.views import UserViewSet, PostViewSet, CommentViewSet
#
# router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)
# router.register(r'post', PostViewSet)
# router.register(r'comment', CommentViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
from django.urls import path

from api2 import views

urlpatterns = [
    path('post/', views.PostListAPIView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostRetrieveAPIView.as_view(), name='post-detail'),
    # url patter 에 pk 가 없는 경우 name postfix 를 -list 로 하는 것이 관례
    path('comment/', views.CommentCreateAPIView.as_view(), name='comment-list')
]
