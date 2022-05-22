from django.contrib import admin

from todos import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'completed', 'created_at', 'updated_at')
    list_filter = ('completed', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)



