#!/bin/bash

# It is responsability of the deployment orchestration to execute before
# migrations, create default admin user, populate minimal data, etc.

gunicorn notes_service.wsgi --config notes_service/gunicorn_conf.py
