from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from news.models import News
from news.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_permissions(self):
        if (self.action == 'create') or (self.action == 'delete'):
            return (IsAdminUser(), )
        else:
            return (AllowAny(), )
