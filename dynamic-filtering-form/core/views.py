from django.db.models import Q
from django.shortcuts import render

from core.models import Category, Journal
from core.filters import JournalFilter


def boostrap_filter_view(request):
    title_contains = request.GET.get('title_contains', None)
    title_exact = request.GET.get('title_exact', None)
    title_or_author = request.GET.get('title_or_author', None)
    view_count_min = request.GET.get('view_count_min', None)
    view_count_max = request.GET.get('view_count_max', None)
    publish_date_min = request.GET.get('publish_date_min', None)
    publish_date_max = request.GET.get('publish_date_max', None)
    category = request.GET.get('category', None)
    reviewed = request.GET.get('reviewed', None) == 'on'

    qs = Journal.objects.all()

    if title_contains:
        qs = qs.filter(title__icontains=title_contains)

    if title_exact:
        qs = qs.filter(title__exact=title_exact)

    if title_or_author:
        qs = qs.filter(
            Q(title__icontains=title_or_author) |
            Q(author__icontains=title_or_author)
        )

    if view_count_min:
        qs = qs.filter(view_count__gte=view_count_min)

    if view_count_max:
        qs = qs.filter(view_count__lte=view_count_max)

    if publish_date_min:
        qs = qs.filter(publish_date__gte=publish_date_min)

    if publish_date_max:
        qs = qs.filter(publish_date__lte=publish_date_max)

    if category:
        qs = qs.filter(categories__name=category)

    if reviewed:
        qs = qs.filter(reviewed=reviewed)

    categories = Category.objects.all()

    qs = qs.distinct()

    context = { 'journals': qs, 'categories': categories }

    return render(request, 'core/boostrap_filter.html', context)



def automatic_filter_view(request):
    qs = Journal.objects.all()
    context = {
        'filter': JournalFilter(request.GET, queryset=qs),
        'journals': qs,
        'categories': Category.objects.all(),
    }
    return render(request, 'core/filters.html', context)
