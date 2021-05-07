from django.db.models import RestrictedError
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from .models import Exam, ExamCard, Label, Question
from .serializers import (
    ExamDetailSerializer,
    ExamSerializer,
    ExamCardSerializer,
    LabelSerializer,
    QuestionSerializer
)


class ExamViewSet(viewsets.ModelViewSet):
    '''
    Вьюсет для списка экзаменов
    '''
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except RestrictedError:
            data = {'message': 'Невозможно удалить экзамен, содержащий билеты'}
            status_code = HTTP_400_BAD_REQUEST
            return Response(data=data, status=status_code)


class ExamDetailView(generics.RetrieveAPIView):
    '''
    Детальное представление экзамена
    '''
    queryset = Exam.objects.all()
    serializer_class = ExamDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'


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


class ExamcardDetailView(generics.RetrieveAPIView):
    '''
    Детальное представление экзаменационного билета
    '''
    queryset = ExamCard.objects.all()
    serializer_class = ExamCardSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'


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
        queryset = Label.objects.all()
        question = self.request.query_params.get('question')
        if question is not None:
            queryset = queryset.filter(question_id=question)
        return queryset
