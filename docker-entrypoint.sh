#!/bin/bash

#python manage.py migrate                  # Apply database migrations
#python manage.py collectstatic --noinput  # Collect static files

echo Cloning project
git clone -b dev https://github.com/denisvolokh/hello_django_rest.git

echo Installing requirements
pip install -r /srv/hello_django_rest/apps/requirements.txt

# Prepare log files and start outputting logs to stdout
touch /srv/logs/gunicorn.log
touch /srv/logs/access.log
tail -n 0 -f /srv/logs/*.log &

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn /srv/hello_django_rest/wsgi:application \
    --name rest_api \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    --log-file=/srv/logs/gunicorn.log \
    --access-logfile=/srv/logs/access.log \
    "$@"
