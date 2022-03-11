import time

from celery import shared_task, current_task
from okSearch.celery import app

from .scrapping import (
    enter_login_params, 
    get_users_info, 
    enter_search_params,
    get_friends_info,
    get_user_active_info,
    get_users_info_by_id,
    get_users_common_friends,
    get_users_obvious_connection,
    get_users_unobvious_connection,
)


@app.task(bind=True)
def login_ok(self, credentials):
    self.update_state(state='PROGRESS')
    enter_login_params(credentials)

@app.task(bind=True)
def search_ok(self, search_params):
    self.update_state(state='PROGRESS')
    enter_search_params(search_params)
    users_info = get_users_info()
    return users_info

@app.task(bind=True)
def get_user_friends(self, user_friends_id):
    self.update_state(state='PROGRESS')
    friends_info = get_friends_info(user_friends_id)
    return friends_info

@app.task(bind=True)
def get_user_active(self, user_selected_id):
    self.update_state(state='PROGRESS')
    user_active_info = get_user_active_info(user_selected_id)
    return user_active_info

@app.task(bind=True)
def get_user_info_by_ids(self, userIDs):
    self.update_state(state='PROGRESS')
    print(userIDs)
    user_info_by_id = get_users_info_by_id(userIDs)
    return user_info_by_id


@app.task(bind=True)
def get_user_common_friends(self, user_friends_ids):
    self.update_state(state='PROGRESS')
    print(user_friends_ids)
    user_common_friends = get_users_common_friends(user_friends_ids)
    return user_common_friends

@app.task(bind=True)
def get_user_obvious_connections(self, user_obvious_connections_ids):
    self.update_state(state='PROGRESS')
    print(user_obvious_connections_ids)
    user_obvious_connections = get_users_obvious_connection(user_obvious_connections_ids)
    return user_obvious_connections

@app.task(bind=True)
def get_user_unobvious_connections(self, user_unobvious_connections_ids):
    self.update_state(state='PROGRESS')
    print(user_unobvious_connections_ids)
    user_unobvious_connections = get_users_unobvious_connection(user_unobvious_connections_ids)
    return user_unobvious_connections

@app.task(bind=True)
def create_task(self, task_type):
    
    self.update_state(state='PROGRESS',
        meta={'current': 0, 'total': 100})
    time.sleep(int(task_type) * 1000)
