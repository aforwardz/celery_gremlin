import time
from gremlin_test.tasks import graph_query_test, test_one, test_two, test_three

batch_size = 100


def test():
    for i in range(batch_size):
        print('Batch: %d' % i)
        graph_query_test.delay()


def test_batch(batch_size=batch_size):
    for i in range(batch_size):
        print('Batch: %d' % i)
        test_one.delay((i,))
        test_two.delay((i,))
        test_three.delay((i,))
