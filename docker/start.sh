#!/bin/bash

set -e

while ! (timeout 3 bash -c "</dev/tcp/${DB_HOST}/${DB_PORT}") &> /dev/null;
do
    echo waiting for PostgreSQL to start...;
    sleep 3;
done;

./manage.py makemigrations --merge  --no-input --traceback
./manage.py migrate  --no-input --traceback
./manage.py collectstatic --no-input --traceback
#daphne -b 0.0.0.0 -p 8000 lifeline.asgi:application
