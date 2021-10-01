#!/bin/bash
PROJECT_ROOT="$(cd $(dirname $0)/..; pwd)"

cd "$PROJECT_ROOT"

docker run -ti -v "${PROJECT_ROOT}:/usr/src/app" --env-file "${PROJECT_ROOT}/.env" mysite:latest python manage.py test $@
