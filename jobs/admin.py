from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'job_type', 'salary',
                    'closing_date', 'created', 'updated']
