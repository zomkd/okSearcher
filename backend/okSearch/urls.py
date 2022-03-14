from django.contrib import admin
from django.urls import path
from okParser.views import (
    get_status, 
    set_credentials, 
    set_search_params, 
    set_user_friends, 
    set_user_active,
    set_user_by_ids,
    set_user_common_friends,
    set_user_obvious_connections,
    set_user_unobvious_connections,
    set_analys_active_users
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("tasks/<task_id>/", get_status, name="get_status"),
    # path("tasks/", run_task, name="run_task"),
    path('login/', set_credentials, name="set_credentials"),
    path('search/', set_search_params, name="set_search_params"),
    path('user_friends/', set_user_friends, name="set_user_friends"),
    path('user_active/', set_user_active, name="set_user_active"),
    path('searchByID/', set_user_by_ids, name="set_user_by_ids"),
    path('user_common_friends/', set_user_common_friends, name="set_user_common_friends"),
    path('user_obvious_connections/', set_user_obvious_connections, name="set_user_obvious_connections"),
    path('user_unobvious_connections/', set_user_unobvious_connections, name="set_user_unobvious_connections"),
    path('analys_active_users/', set_analys_active_users, name="set_analys_active_users"),
    
    # path('users/', )
]
