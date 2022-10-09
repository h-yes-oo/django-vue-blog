# Routers provide an easy way of automatically determining the URL conf.
from django.urls import path, include
from rest_framework import routers

from api2.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # 아래 줄은 단순히 화면에 로그인 버튼을 보여주는 역할을 할 뿐
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]