from django.contrib import admin
from django.urls import path, include

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api2/', include('api2.urls')),

    # path('', include(router.urls)),
    # 아래 줄은 단순히 화면에 로그인 버튼을 보여주는 역할을 할 뿐
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
