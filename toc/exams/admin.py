from django.contrib import admin
from .models import (
    Exam,
    ExamCard,
)


admin.site.register(Exam)
admin.site.register(ExamCard)
