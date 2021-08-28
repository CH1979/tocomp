from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    content = models.TextField(
        null=True,
        blank=True,
        default='Lorem ipsum'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.RESTRICT
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    image = models.ImageField(
        upload_to='uploads/%Y/'
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'News'
