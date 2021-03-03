from django.contrib import admin
from .models import (
    Exam,
    ExamCard,
    LabelsForAnswerChoice,
    Question
)


admin.site.register(Exam)
admin.site.register(ExamCard)
# admin.site.register(LabelsForAnswerChoice)
# admin.site.register(Question)


class LabelsInline(admin.TabularInline):
    model = LabelsForAnswerChoice
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('exam_card', 'title', 'content', 'answer_type')
    inlines = [LabelsInline]

    class Media:
        js = ('js/hide_inlines.js',)
