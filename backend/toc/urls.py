from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from exams.urls import router as exams_router
from news.urls import router as news_router


router = DefaultRouter()
router.registry.extend(exams_router.registry)
router.registry.extend(news_router.registry)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
] \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Перечитать https://docs.djangoproject.com/en/3.1/howto/static-files/
# перед переносом в прод
