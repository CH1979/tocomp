from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Exam


class ExamCreate(CreateView):
    model = Exam
    success_url = reverse_lazy('')
