from django.contrib import admin
from .models import Course, GroupDetail


admin.site.register(Course)


@admin.register(GroupDetail)
class GroupDetailAdmin(admin.ModelAdmin):
    list_display = ('year', 'course')
