from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Exam


class ExamCreateView(CreateView):
    model = Exam
    fields = '__all__'
    success_url = reverse_lazy('exam-list')


class ExamUpdateView(UpdateView):
    model = Exam
    fields = '__all__'
    success_url = reverse_lazy('exam-list')


class ExamDeleteView(DeleteView):
    model = Exam
    success_url = reverse_lazy('exam-list')


class ExamListView(ListView):
    model = Exam
    context_object_name = 'exam_list'
    queryset = Exam.objects.annotate(num_cards=Count('examcard'))


class ExamDetailView(DetailView):
    model = Exam
