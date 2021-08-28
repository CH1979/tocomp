from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register(r'exams', views.ExamViewSet, basename='exams')
router.register(r'examcards', views.ExamCardViewSet, basename='examcards')
router.register(r'questions', views.QuestionViewSet, basename='questions')

urlpatterns = [
    path(
        'exams/<int:pk>/detail/',
        views.ExamDetailView.as_view(),
        name='exam-detail'
    ),
    path(
        'examcards/<int:pk>/detail/',
        views.ExamcardDetailView.as_view(),
        name='examcard-detail'
    ),
    path(
        '',
        include(router.urls)
    ),
]
