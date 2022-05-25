import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict

from tasks.models import Task


def list_all_tasks(request):
    data = {
        'tasks': []
    }

    for task in Task.objects.all():
        data['tasks'].append(task.to_json())

    return JsonResponse(data)

@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'DELETE':
        get_object_or_404(Task, pk=task_id).delete()
        return JsonResponse({}, status=204)
    return HttpResponseNotAllowed(['DELETE'])


@csrf_exempt
def update_task(request, task_id):
    if request.method != 'PUT':
        return HttpResponseNotAllowed(['PUT'])

    task = get_object_or_404(Task, pk=task_id)
    data = QueryDict(request.body)

    task.name = data.get('name', task.name)
    percentage_completed = data.get('percentage_completed', task.percentage_completed)

    if isinstance(percentage_completed, str):
        percentage_completed = percentage_completed.strip()
        percentage_completed = percentage_completed.replace('%', '')
        percentage_completed = int(percentage_completed)

    if not isinstance(percentage_completed, int):
        return JsonResponse({
            'error': 'percentage_completed must be an integer',
            'task': task.to_json(),
        }, status=400)

    if not (0 <= percentage_completed <= 100):
        return JsonResponse({
            'error': 'percentage_completed must be between 0 and 100',
            'task': task.to_json(),
        }, status=400)

    task.percentage_completed = percentage_completed
    task.save()

    return JsonResponse({
        'task': task.to_json(),
    }, status=204)



@csrf_exempt
def create_task(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    data = QueryDict(request.body)

    name = data.get('name', '')
    percentage_completed = data.get('percentage_completed', 0)

    if isinstance(percentage_completed, str):
        percentage_completed = percentage_completed.strip()
        percentage_completed = percentage_completed.replace('%', '')
        percentage_completed = int(percentage_completed)

    if not isinstance(percentage_completed, int):
        return JsonResponse({
            'error': 'percentage_completed must be an integer',
        }, status=400)

    if not (0 <= percentage_completed <= 100):
        return JsonResponse({
            'error': 'percentage_completed must be between 0 and 100',
        }, status=400)

    task = Task.objects.create(name=name, percentage_completed=percentage_completed)

    return JsonResponse({
        'task': task.to_json(),
    }, status=201)