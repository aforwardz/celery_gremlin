# coding: utf-8
from __future__ import absolute_import, unicode_literals
import traceback
import time
from gremlin_test.celery import app
from gremlin_test.client import client


@app.task(queue='test', default_retry_delay=1 * 60)
def graph_query_test():

    dsl = """g.V().limit(1)"""
    time.sleep(0.5)
    try:
        res = client.submit(dsl).one()
        if res and res[0]:
            print(res[0])
    except:
        print(traceback.format_exc())
