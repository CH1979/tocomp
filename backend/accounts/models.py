from django.contrib.auth.models import Group, User
from django.db import models

from exams.models import Exam, ExamCard


class Course(models.Model):
    '''
    Направление обучение (кружок)
    '''
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )
    short_name = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return f'{self.name}'


class GroupDetail(Group):
    '''
    Дополнительная информация по группам учащихся
    '''
    name = None
    year = models.IntegerField(
        blank=False,
        null=False
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.RESTRICT,
        blank=False,
        null=False
    )

    def __str__(self):
        return f'{self.year}-{self.course}'

    class Meta:
        unique_together = ('year', 'course')


class ExamEvent(models.Model):
    '''
    Расписание экзаменов для групп
    '''
    exam = models.ForeignKey(
        Exam,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    ),
    group = models.ForeignKey(
        GroupDetail,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    start_at = models.DateTimeField()
    finish_at = models.DateTimeField()
    examiner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )


class Ticket(models.Model):
    '''
    Распределение билетов между экзаменуемыми
    '''
    examevent = models.ForeignKey(
        ExamEvent,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    examcard = models.ForeignKey(
        ExamCard,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    examinee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
