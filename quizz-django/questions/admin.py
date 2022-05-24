from django.contrib import admin

from questions import models


class AnswerInline(admin.TabularInline):
    model = models.Answer


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]


admin.site.register(models.Answer)
