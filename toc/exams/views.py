from rest_framework import viewsets
from .models import Exam, ExamCard, LabelForChoice, Question
from .serializers import (
    ExamSerializer,
    ExamCardSerializer,
    LabelSerializer,
    QuestionSerializer
)


class ExamViewSet(viewsets.ModelViewSet):
    '''
    Вьюсет для тем экзаменов
    '''
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamCardViewSet(viewsets.ModelViewSet):
    '''
    Вьюсет для экзаменационных билетов
    '''
    serializer_class = ExamCardSerializer

    def get_queryset(self):
        queryset = ExamCard.objects.all()
        exam = self.request.query_params.get('exam')
        if exam is not None:
            queryset = queryset.filter(exam_id=exam)
        return queryset


class QuestionViewSet(viewsets.ModelViewSet):
    '''
    Вьюсет для экзаменационных билетов
    '''
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        examcard = self.request.query_params.get('examcard')
        if examcard is not None:
            queryset = queryset.filter(examcard_id=examcard)
        return queryset


class LabelViewSet(viewsets.ModelViewSet):
    '''
    Вьюсет для меток вариантов ответа
    '''
    serializer_class = LabelSerializer

    def get_queryset(self):
        queryset = LabelForChoice.objects.all()
        question = self.request.query_params.get('question')
        if question is not None:
            queryset = queryset.filter(question_id=question)
        return queryset
