from .types import Credentials
from .tasks import login_ok
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

credentials = Credentials()

@csrf_exempt
def set_credentials(request):
    task = ''
    if request.method == 'POST':
        ok_credentilas = set_ok_credentials()
        ok_credentilas['username'] = request.POST.get('username','')
        ok_credentilas['password'] = request.POST.get('password','')
        credentials = Credentials(**ok_credentilas)
        task = login_ok.delay(credentials.dict())
        print(task.id)
        return JsonResponse({'msg': 'Login is success!','task_id': task.id}, status=200)
    # if request.method == 'GET':
    #     return JsonResponse({'msg': "Login is success!","task_id": task.id}, status=200)
    return JsonResponse({'msg': "Login is fail!"}, status=400)

def set_ok_credentials(): #TODO не должно задаваться в ручуную
    return 'enter cred'




