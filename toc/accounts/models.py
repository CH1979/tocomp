from django.contrib.auth.models import Group
from django.core.validators import RegexValidator
from django.db import models


class Period(models.Model):
    '''
    Учебный год
    '''
    year = models.CharField(
        max_length=9,
        blank=False,
        null=False,
        unique=True,
        validators=[
            RegexValidator(
                '^\d{4}/\d{4}$',  # noqa
                message="Введите учебный год в формате ГГГГ/ГГГГ"
                )
        ]
    )

    def __str__(self):
        return f'{self.year}'


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

    def __str__(self):
        return f'{self.name}'


class GroupDetail(Group):
    '''
    Дополнительная информация по группам учащихся
    '''
    name = None
    year = models.ForeignKey(
        Period,
        on_delete=models.RESTRICT,
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
