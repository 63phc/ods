#!/bin/bash

echo "RUN migrate collectstatic compilemessages"
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py compilemessages
gunicorn src.wsgi:application -b 0.0.0.0:8080