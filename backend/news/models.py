from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    content = RichTextUploadingField()
    author = models.ForeignKey(
        User,
        on_delete=models.RESTRICT
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'News'
