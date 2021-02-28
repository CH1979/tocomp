from django.contrib import admin
from .models import Course, GroupDetail, Period


admin.site.register(Course)
admin.site.register(Period)


@admin.register(GroupDetail)
class GroupDetailAdmin(admin.ModelAdmin):
    list_display = ('year', 'course')
