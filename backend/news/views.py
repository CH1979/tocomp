from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_permissions(self):
        if (self.action == 'create') or (self.action == 'delete'):
            return (IsAdminUser(), )
        else:
            return (AllowAny(), )
