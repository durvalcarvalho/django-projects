# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Repository, Commit


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'modified', 'name', 'user', 'star')
    list_filter = ('created', 'modified', 'user')
    search_fields = ('name',)


@admin.register(Commit)
class CommitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'user',
        'repository',
        'code',
        'hash_value',
    )
    list_filter = ('created', 'modified', 'user', 'repository')
