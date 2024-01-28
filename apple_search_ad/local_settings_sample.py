# SITE_URL = 'http://172.105.54.227'
SITE_URL = 'http://localhost:8000'
# SITE_URL = 'http://localhost:8000'

# The location of all the media files like img, video etc
# MEDIA_ROOT = '/Users/jahangir/Documents/media_directory/'
MEDIA_ROOT = '/Users/datasecurity/Documents/media_directory/apple_search_ad_project/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'apple_searchad',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'logo': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'logomaker_apple_search_ad',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'campaign.apps.CampaignConfig',
    'rest_framework',
    'django_crontab',
]

