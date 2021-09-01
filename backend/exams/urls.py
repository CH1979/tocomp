from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'exams', views.ExamViewSet, basename='exams')
router.register(r'examcards', views.ExamCardViewSet, basename='examcards')
router.register(r'questions', views.QuestionViewSet, basename='questions')
