from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'news', views.NewsViewSet, basename='news')
