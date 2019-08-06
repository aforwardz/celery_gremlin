from gremlin_python.driver import client

try:
    client = client.Client('ws://127.0.0.1:8182/gremlin', 'g', pool_size=1)
except:
    client = None
