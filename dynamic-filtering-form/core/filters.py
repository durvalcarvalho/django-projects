import django_filters
from django.db import models

from core.models import Journal


class JournalFilter(django_filters.FilterSet):
    class Meta:
        model = Journal
        fields = {
            'title': [
                'icontains',
                'exact',
            ],
            'author__name': [
                'icontains',
                'exact',
            ],

            'categories': ['exact'],
            'reviewed': ['exact'],
            'publish_at': ['gte', 'lte'],
            'views': ['gte', 'lte'],
        }