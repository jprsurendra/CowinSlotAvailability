https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04


ALLOWED_HOSTS = ['*']

import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')







python manage.py  makemigrations
python manage.py  migrate

python manage.py createsuperuser --email jpr_surendra@yahoo.co.in
UserName: jpr_surendra
Password: Rathore@39
Password(again): Rathore@39




pip install requests

