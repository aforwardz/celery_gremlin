# coding:utf8
from __future__ import absolute_import
import sys
import os
from datetime import timedelta

from celery import Celery, Task
from celery.schedules import crontab
from kombu import Queue


class CustomCelery(Celery):
    def __init__(self, *args, **kwargs):
        super(CustomCelery, self).__init__(*args, **kwargs)


app = CustomCelery('gremlin_test')


class CeleryConfig(object):
    BROKER_URL = 'redis://127.0.0.1:6379/0'
    CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERYD_CONCURRENCY = 8
    CELERYD_MAX_TASKS_PER_CHILD = 10

    CELERY_INCLUDE = ['gremlin_test.tasks']

    CELERY_QUEUES = (
        Queue('test',),
    )

# Using a string here means the worker will not have to
# pickle the object when using Windows.


app.config_from_object(CeleryConfig)
print('Celery Start!!')
app.control.purge()

if __name__ == '__main__':
    app.start()
    print('Celery Start!!')
    app.control.purge()
