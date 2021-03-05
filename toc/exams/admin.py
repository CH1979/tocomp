from django.contrib import admin
from .models import (
    Exam,
    ExamCard,
    LabelsForChoice,
    Question
)


admin.site.register(Exam)
admin.site.register(ExamCard)


class LabelsInline(admin.TabularInline):
    model = LabelsForChoice
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('exam_card', 'title', 'content', 'answer_type')
    inlines = [LabelsInline]

    class Media:
        js = ('js/hide_inlines.js',)
