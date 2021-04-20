from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'exams', views.ExamViewSet)
router.register(r'examcards', views.ExamCardViewSet, basename='examcards')
router.register(r'questions', views.QuestionViewSet, basename='questions')
router.register(r'labels', views.LabelViewSet, basename='labels')

urlpatterns = [
    path('', include(router.urls)),
]
