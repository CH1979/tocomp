from django.contrib import admin
from .models import (
    Exam,
    ExamCard,
    LabelForChoice,
    Question
)


admin.site.register(Exam)
admin.site.register(ExamCard)
admin.site.register(LabelForChoice)
admin.site.register(Question)
