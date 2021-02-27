from django.contrib.auth.models import Group, User
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


class GroupExtended(models.Model):
    '''
    Дополнительная информация по группам учащихся
    '''
    group = models.OneToOneField(Group)
    year = models.ForeignKey(
        Period,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    teacher = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        limit_choices_to={'is_staff': True}
    )

    def __str__(self):
        return f'{self.year}-{self.course}'
