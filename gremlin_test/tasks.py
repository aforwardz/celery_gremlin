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


@app.task(queue='test_one')
def test_one(batch):
    print('Test One & Batch %s' % batch)
    time.sleep(0.2)


@app.task(queue='test_two')
def test_two(batch):
    print('Test Two & Batch %s' % batch)
    time.sleep(5)


@app.task(queue='test_three')
def test_three(batch):
    print('Test Three & Batch %s' % batch)
    time.sleep(1)
