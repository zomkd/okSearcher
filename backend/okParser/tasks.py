import time

from celery import shared_task, current_task
from okSearch.celery import app

@app.task(bind=True)
def create_task(self, task_type):
    
    self.update_state(state='PROGRESS',
        meta={'current': 0, 'total': 100})
    time.sleep(int(task_type) * 1000)
