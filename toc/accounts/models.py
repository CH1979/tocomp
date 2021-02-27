from django.db import models
from django.contrib.auth.models import Group


class GroupExtended(models.Model):
    group = models.OneToOneField(Group)
