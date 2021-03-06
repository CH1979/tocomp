from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.ExamCreate.as_view(), name='exam-create')
]
