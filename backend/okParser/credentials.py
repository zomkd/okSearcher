from .types import Credentials
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# credentials = Credentials()

def set_ok_credentials(): #TODO не должно задаваться в ручуную
    return {
        'application_id': '512001008108', 
        'application_key': 'CNOCGEKGDIHBABABA', 
        'application_secret_key': '18B01FDF9A5084AFA1669DDB',
        'session_key': 'tkn1EhliRxCEAvwDOeURwKjZU3ArOtKp15kUfrs4IkgZknRO3FNiQpBqGETq4tuK4FnC3',
        'session_secret_key': '61db37441d2c3d823f7aee91a1104b97',
        }
