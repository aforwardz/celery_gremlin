#!/bin/sh

one="logs/celery/one_worker.pid"
if [ -f "$one" ]; then
    rm "$one"
    echo "DELETE ONE WORKER PID"
fi

two="logs/celery/two_worker.pid"
if [ -f "$two" ]; then
    rm "$two"
    echo "DELETE TWO WORKER PID"
fi

three="logs/celery/three_worker.pid"
if [ -f "$three" ]; then
    rm "$three"
    echo "DELETE THREE WORKER PID"
fi

ps auxww | grep 'celery worker' | awk '{print $2}' | xargs kill -9
echo "KILL ALL CELERY"

celery -A gremlin_test multi start one_worker two_worker three_worker -l info -f logs/celery/%n.log --pidfile=logs/celery/%n.pid -Q:one_worker test_one -Q:two_worker test_two -Q:three_worker test_three