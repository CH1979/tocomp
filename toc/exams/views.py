from django.db.models import Count, Max
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Exam, ExamCard, Question, LabelForChoice


class ExamCreateView(CreateView):
    '''
    Создание тем экзаменов
    '''
    model = Exam
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('exam-detail', kwargs={'pk': self.object.id})


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
    current_examcard_num = ExamCard.objects.filter(
        exam__id=exam
    ).aggregate(
        Max('number')
    )['number__max']

    if current_examcard_num is None:
        new_examcard_num = 1
    else:
        new_examcard_num = current_examcard_num + 1

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
    fields = ('title', 'content', 'answer_type')

    def get_success_url(self):
        answer_type = self.object.answer_type
        if answer_type in ['TA', 'SF']:
            success_url = reverse_lazy(
                'examcard-detail',
                kwargs={
                    'exam': self.object.examcard.exam_id,
                    'pk': self.object.examcard_id
                }
            )
        else:
            success_url = reverse_lazy(
                'question-detail',
                kwargs={
                    'exam': self.object.examcard.exam_id,
                    'examcard': self.object.examcard_id,
                    'pk': self.object.id
                }
            )
        return success_url

    def form_valid(self, form):
        examcard = get_object_or_404(ExamCard, pk=self.kwargs['examcard'])
        form.instance.examcard = examcard
        return super(QuestionCreateView, self).form_valid(form)


class QuestionDetailView(DetailView):
    model = Question


class LabelCreateView(CreateView):
    model = LabelForChoice
    fields = ('label',)

    def get_success_url(self):
        return reverse_lazy(
            'question-detail',
            kwargs={
                'exam': self.object.question.examcard.exam_id,
                'examcard': self.object.question.examcard_id,
                'pk': self.object.question_id
            }
        )

    def form_valid(self, form):
        question = get_object_or_404(Question, pk=self.kwargs['pk'])
        form.instance.question = question
        return super(LabelCreateView, self).form_valid(form)
