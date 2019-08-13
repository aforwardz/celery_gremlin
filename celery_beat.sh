#!/bin/sh

## To start the celery beat service:
##
## $ celery -A proj beat
## You can also embed beat inside the worker by enabling the workers -B option,
## this is convenient if you’ll never run more than one worker node, but it’s not
## commonly used and for that reason isn’t recommended for production use:
##
## $ celery -A proj worker -B


celery -A gremlin_test beat -l info -f logs/celery/celery_beat.log