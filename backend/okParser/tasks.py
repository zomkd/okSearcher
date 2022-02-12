import time

from celery import shared_task, current_task
from okSearch.celery import app

import undetected_chromedriver as uc


driver = uc.Chrome()

@app.task(bind=True)
def login_ok(self, credentials):
    self.update_state(state='PROGRESS')
    driver.get('https://ok.ru/')
    driver.find_element_by_id("field_email").send_keys(credentials['username'])
    driver.find_element_by_id("field_password").send_keys(credentials['password'])
    driver.find_element_by_xpath("//input[@value='Log in to OK']").click()

@app.task(bind=True)
def create_task(self, task_type):
    
    self.update_state(state='PROGRESS',
        meta={'current': 0, 'total': 100})
    time.sleep(int(task_type) * 1000)
