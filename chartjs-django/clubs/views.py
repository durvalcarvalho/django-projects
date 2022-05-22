import json
from django.views import generic

from clubs.models import Club


class ClubChartView(generic.TemplateView):
    template_name = 'clubs/chart.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clubs'] = Club.objects.all()

        chart_spec = {
            "type": "bar",
            "data": {
                "labels": [club.name for club in Club.objects.all()],
                "datasets": [{
                    "label": "Revenue (millions)",
                    "data": [club.money for club in Club.objects.all()],
                }],
                "backgroundColor": [
                    "rgba(255, 99, 132, 0.2)",
                    "rgba(54, 162, 235, 0.2)",
                    "rgba(255, 206, 86, 0.2)",
                    "rgba(75, 192, 192, 0.2)",
                    "rgba(153, 102, 255, 0.2)",
                    "rgba(255, 159, 64, 0.2)",
                ],
                "borderColor": [
                    "rgba(255, 99, 132, 1)",
                    "rgba(54, 162, 235, 1)",
                    "rgba(255, 206, 86, 1)",
                    "rgba(75, 192, 192, 1)",
                    "rgba(153, 102, 255, 1)",
                    "rgba(255, 159, 64, 1)",
                ],
                "borderWidth": 1
            },
            "options": {
                "scales": {
                    "y": { "beginAtZero": "true" }
                }
            }
        }

        context['chart_spec'] = json.dumps(chart_spec)

        return context
