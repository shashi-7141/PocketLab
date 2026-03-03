from django.contrib import admin
from .models import ExperimentLog


@admin.register(ExperimentLog)
class ExperimentLogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at')
    list_filter = ('date',)
    search_fields = ('title', 'observations', 'results')
    ordering = ('-date',)