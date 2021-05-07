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
        unique=True,
        verbose_name='Тема экзамена'
    )

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'

    def __str__(self):
        return f'{self.theme}'


class ExamCard(models.Model):
    '''
    Экзаменационный билет
    '''
    exam = models.ForeignKey(
        Exam,
        related_name='examcards',
        on_delete=models.CASCADE,
    )
    number = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('exam', 'number')
        ordering = ['number']

    def __str__(self):
        return f'{self.exam} - билет № {self.number}'


class Question(models.Model):
    '''
    Содержание вопроса и указание типа ответа
    '''
    examcard = models.ForeignKey(
        ExamCard,
        related_name='questions',
        on_delete=models.RESTRICT
    )
    content = models.TextField(
        null=True,
        blank=True
    )
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


class Label(models.Model):
    '''
    Варианты ответа
    '''
    question = models.ForeignKey(
        Question,
        related_name='labels',
        on_delete=models.CASCADE
    )
    text = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    is_correct = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'{self.label}'


class Choice(models.Model):
    '''
    Выбранные варианты ответов
    '''
    choice = models.ForeignKey(Label, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UploadedFiles(models.Model):
    '''
    Ответы в виде файлов
    '''
    file = models.FileField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
