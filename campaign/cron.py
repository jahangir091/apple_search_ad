
# python manage.py crontab add
# python manage.py crontab show
# python manage.py crontab remove
# https://pypi.org/project/django-crontab/

import random
import string

from django.contrib.auth.models import User


def my_scheduled_job():
    username = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=10))
    u = User(username=username)
    u.save()
    print("cron is running fine!")

