from django.db.models import Count, Max
from django.http.response import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Exam, ExamCard, Question


class ExamCreateView(CreateView):
    '''
    Создание тем экзаменов
    '''
    model = Exam
    fields = '__all__'
    success_url = reverse_lazy('exam-list')


class ExamUpdateView(UpdateView):
    '''
    Изменение тем экзаменов
    '''
    model = Exam
    fields = '__all__'
    success_url = reverse_lazy('exam-list')


class ExamDeleteView(DeleteView):
    '''
    Удаление тем экзаменов
    '''
    model = Exam
    success_url = reverse_lazy('exam-list')


class ExamListView(ListView):
    '''
    Полный список тем экзаменов
    '''
    model = Exam
    context_object_name = 'exam_list'
    queryset = Exam.objects.annotate(num_cards=Count('examcard'))


class ExamDetailView(DetailView):
    '''
    Список билетов по выбранной теме экзамена
    '''
    model = Exam
    context_object_name = 'exam'

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Exam.objects.filter(pk=pk).order_by('-examcard')
        return queryset


class ExamCardDetailView(DetailView):
    '''
    Список вопросов в выбранном билете
    '''
    model = ExamCard
    context_object_name = 'examcard'

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = ExamCard.objects.filter(pk=pk)
        return queryset


def examcard_create_view(request, exam):
    '''
    Создание нового экзаменационного билета
    '''
    current_exam = ExamCard.objects.filter(exam__id=exam)
    if current_exam is None:
        new_examcard_num = 1
    else:
        max_examcard_num = current_exam.aggregate(Max('number'))
        new_examcard_num = max_examcard_num['number__max'] + 1

    new_examcard = ExamCard(
        exam=Exam.objects.get(id=exam),
        number=new_examcard_num
    )
    new_examcard.save()

    return HttpResponseRedirect(reverse(
        'examcard-detail',
        kwargs={'exam': exam, 'pk': new_examcard.id}
    ))


class ExamCardDeleteView(DeleteView):
    '''
    Удаление экзаменационного билета
    '''
    model = ExamCard

    def get_success_url(self):
        return reverse_lazy('exam-detail', kwargs={'pk': self.object.exam_id})


class QuestionCreateView(CreateView):
    '''
    Добавление вопросов в билет
    '''
    model = Question
    fields = '__all__'
    success_url = reverse_lazy('examcard-detail')
