from django.contrib import admin

from core import models


admin.site.register(models.Author)
admin.site.register(models.Category)
admin.site.register(models.Journal)
