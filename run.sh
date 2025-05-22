#!/bin/bash

python manage.py makemigrations

python manage.py migrate

python manage.py fake_demo

python manage.py runserver

