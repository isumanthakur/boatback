#!/bin/sh

if [ "$DATABASE" = "postgres" ] 
then
    echo "Waiting for PostgreSQL to start..."

    echo "Using SQL_HOST: $SQL_HOST and SQL_PORT: $SQL_PORT"

    while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
        sleep 1
    done

    echo "PostgreSQL is up and running :-D"
fi

# Collect static files
python manage.py collectstatic --noinput

python manage.py makemigrations
python manage.py migrate

# Start Gunicorn server, binding it to port 10000
exec gunicorn --bind 0.0.0.0:$PORT djangobnb_backend.wsgi:application
