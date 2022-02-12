from celery.result import AsyncResult
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from celery.result import AsyncResult

from okParser.tasks import create_task

@csrf_exempt
def run_task(request):
    if request.method == 'POST':
        task_type = request.body.decode("utf-8") 
        task = create_task.delay(int(1))
        return JsonResponse({"task_id": task.id,"current": task.info}, status=202)
    return HttpResponse(request)


@csrf_exempt
def get_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
        # "current": task_result.info.get('current')
    }
    return JsonResponse(result, status=200) 