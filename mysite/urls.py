from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mysite.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls')),
    path('api/', include('api.urls')),

    path('api2/', include('api2.urls')),

    # path('', include(router.urls)),
    # 아래 줄은 단순히 화면에 로그인 버튼을 보여주는 역할을 할 뿐
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
