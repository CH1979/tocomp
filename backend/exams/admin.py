from django.contrib import admin
from .models import (
    Exam,
    ExamCard,
    Label,
    Question
)


admin.site.register(Exam)
admin.site.register(ExamCard)
admin.site.register(Label)
admin.site.register(Question)
