import calendar

from django.shortcuts import render
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.utils import timezone

import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

from repository.models import Commit
from repository.utils import date_range


@login_required
def commits(request):
    commits = Commit.objects.filter(user=request.user).order_by('created')

    now = timezone.now()
    start = now - timezone.timedelta(days=363)
    commits = commits.filter(created__range=[start, now])

    # Truncate datetime to date
    commits = commits.annotate(date=TruncDate('created'))

    count = commits.values('date').annotate(count=Count('date')).order_by('date')

    df = pd.DataFrame(list(count))
    df.set_index('date', inplace=True)
    df.index = pd.to_datetime(df.index)

    idx = pd.date_range(start=start, end=now).date
    df = df.reindex(idx, fill_value=0)

    weekdays = [[] for _ in range(7)]
    dates = [[] for _ in range(7)]

    for date, count in df.iterrows():
        i = date.weekday()
        weekdays[i].append(int(count))
        dates[i].append(date)

    day_names = list(calendar.day_name)


    first_day = df.index[0].weekday()
    days = day_names[first_day:] + day_names[:first_day]

    fig = go.Figure()

    fig.add_trace(
        go.Heatmap(
            z=weekdays,
            colorscale='greens',
            x=dates[0],
            y=days,
            text=[weekdays, dates],
            hovertemplate='%{ text[0]:.0f } contributions on %{ text[1] }',
            # height=320,
            # width=1300,
            # hover_data=['count'],
        )
    )

    # set figure height and width
    fig.update_layout(height=320, width=1300)
    fig.update_traces(showscale=False)



    # fig = px.imshow(
    #     weekdays,
    #     color_continuous_scale='greens',
    #     x=dates[0],
    #     y=days,
    #     height=320,
    #     width=1300,
    #     hover_data=['count'],
    # )
    fig.update_layout(plot_bgcolor='white')
    fig.update_traces({'xgap': 5, 'ygap': 5})
    chart = fig.to_html()

    context = { 'commits': commits, 'chart': chart }
    return render(request, 'repository/commits.html', context)

