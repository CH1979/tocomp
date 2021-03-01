from django.views import generic
from .models import News


class NewsListView(generic.ListView):
    model = News
    context_object_name = 'news_list'
    queryset = News.objects.all()[:5]
