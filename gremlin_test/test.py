import time
from gremlin_test.tasks import graph_query_test

batch_size = 1000


def test():
    for i in range(batch_size):
        print('Batch: %d' % i)
        graph_query_test.delay()



