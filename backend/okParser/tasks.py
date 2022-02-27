import time

from celery import shared_task, current_task
from okSearch.celery import app

from .scrapping import enter_login_params, get_users_info, enter_search_params,get_friends_info,get_user_active_info


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
def create_task(self, task_type):
    
    self.update_state(state='PROGRESS',
        meta={'current': 0, 'total': 100})
    time.sleep(int(task_type) * 1000)
