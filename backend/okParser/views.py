from django.http import JsonResponse
from .types import SearchParams
from django.views.decorators.csrf import csrf_exempt
from celery.result import AsyncResult
from .tasks import login_ok, search_ok, get_user_friends, get_user_active
from .credentials import set_ok_credentials
from okParser.tasks import create_task


searchParams = SearchParams()
ok_credentilas = {}

@csrf_exempt
def set_credentials(request):
    task = ''
    if request.method == 'POST':
        ok_credentilas = set_ok_credentials()
        ok_credentilas['username'] = request.POST.get('username','')
        ok_credentilas['password'] = request.POST.get('password','')
        # credentials = Credentials(**ok_credentilas)
        task = login_ok.delay(ok_credentilas)
        print(task.id)
        return JsonResponse({'msg': 'Login is success!','task_id': task.id}, status=200)
    return JsonResponse({'msg': "Login is fail!"}, status=400)

@csrf_exempt
def set_search_params(request):
    if request.method == 'POST':
        ok_searchParams = {}
        ok_searchParams['firstname'] = request.POST.get('firstname','')
        ok_searchParams['secondname'] = request.POST.get('secondname','')
        ok_searchParams['fromAge'] = request.POST.get('fromAge','')
        ok_searchParams['tillAge'] = request.POST.get('tillAge','')
        ok_searchParams['city'] = request.POST.get('city','')
        ok_searchParams['country'] = request.POST.get('country','')
        searchParams = SearchParams(**ok_searchParams)
        task = search_ok.delay(searchParams.dict())

        return JsonResponse({'msg': 'Search is success!','task_id': task.id}, status=200)

    return JsonResponse({'msg': "Search is fail!"}, status=400)

@csrf_exempt
def set_user_friends(request):
    if request.method == 'POST':
        user_friends_id = []
        selected = request.POST.get('selected_users','')
        user_friends_id.append(selected)
        print(user_friends_id)
        task = get_user_friends.delay(user_friends_id)

        return JsonResponse({'msg': 'User friends is success!','task_id': task.id}, status=200)

    return JsonResponse({'msg': "Search is fail!"}, status=400)

@csrf_exempt
def set_user_active(request):
    if request.method == 'POST':
        user_selected_id = []
        selected = request.POST.get('selected_users','')
        user_selected_id.append(selected)
        print(user_selected_id)
        task = get_user_active.delay(user_selected_id)

        return JsonResponse({'msg': 'User active is success!','task_id': task.id}, status=200)

    return JsonResponse({'msg': "User active is fail!"}, status=400)


#TODO delete this func
@csrf_exempt
def run_task(request):
    if request.method == 'POST':
        task_type = request.body.decode("utf-8") 
        task = create_task.delay(int(1))
        return JsonResponse({"task_id": task.id,"current": task.info}, status=202)
    return 'd'


@csrf_exempt
def get_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        # "task_result": task_result.result,
        "task_data": task_result.get()
        # "current": task_result.info.get('current')
    }
    return JsonResponse(result, status=200) 