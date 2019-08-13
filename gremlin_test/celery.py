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
    CELERYD_CONCURRENCY = 4
    CELERYD_MAX_TASKS_PER_CHILD = 4
    print('CONCURRENCY: %d  &  MAX TASK: %d' % (CELERYD_CONCURRENCY, CELERYD_MAX_TASKS_PER_CHILD))

    CELERY_INCLUDE = ['gremlin_test.tasks']

    CELERY_QUEUES = (
        Queue('test',),
        Queue('test_one', ),
        Queue('test_two', ),
        Queue('test_three', ),
    )

    CELERYBEAT_SCHEDULE = {}
    CELERYBEAT_SCHEDULE.update({
        'test_one_schedule': {
            'task': 'gremlin_test.tasks.test_one',
            'schedule': timedelta(minutes=1),
            'args': (2,)
        },
        'test_two_schedule': {
            'task': 'gremlin_test.tasks.test_two',
            'schedule': timedelta(minutes=1),
            'args': (2,)
        },
        'test_three_schedule': {
            'task': 'gremlin_test.tasks.test_three',
            'schedule': timedelta(minutes=1),
            'args': (2,)
        },
    })

# Using a string here means the worker will not have to
# pickle the object when using Windows.


app.config_from_object(CeleryConfig)
app.control.purge()

