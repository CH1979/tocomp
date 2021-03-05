from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


class Exam(models.Model):
    '''
    Комплект экзаменационных билетов по определенной теме
    '''
    theme = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return f'{self.theme}'


class ExamCard(models.Model):
    '''
    Экзаменационный билет
    '''
    exam = models.ForeignKey(
        Exam,
        on_delete=models.RESTRICT
    )
    number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.exam}. Билет № {self.number}'


class Question(models.Model):
    '''
    Содержание вопроса и указание типа ответа
    '''
    exam_card = models.ForeignKey(
        ExamCard,
        on_delete=models.RESTRICT
    )
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )
    content = RichTextUploadingField()
    ANSWER_TYPES = [
        ('TA', 'Текстовый ответ'),
        ('SC', 'Выбор единственного варианта'),
        ('MC', 'Выбор нескольких вариантов'),
        ('SF', 'Загрузка файла')
    ]
    answer_type = models.CharField(
        max_length=2,
        choices=ANSWER_TYPES,
        default='TA',
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.title}'


class TextAnswer(models.Model):
    '''
    Текстовый ответ
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField()


class LabelsForChoice(models.Model):
    '''
    Варианты ответа
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    label = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )

    def __str__(self):
        return f'{self.label}'


class Choice(models.Model):
    '''
    Выбранные варианты ответов
    '''
    choice = models.ForeignKey(LabelsForChoice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UploadedFiles(models.Model):
    '''
    Ответы в виде файлов
    '''
    file = models.FileField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
