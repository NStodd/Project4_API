#!/usr/bin/env bash

# exit on error
set -o errexit

## Install dependencies
pip install -r dependencies.txt

## Run migrations after installing
python manage.py migrate

