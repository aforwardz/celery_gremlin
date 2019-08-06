#!/bin/sh

celery -A gremlin_test worker -Q test -l info -f celery.log