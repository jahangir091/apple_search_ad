from django.conf import settings

from rest_framework.response import Response
from rest_framework import status


def get_model_manager(model, bundle_id):
    if bundle_id == 'com.bitmorpher.apps.logomaker':
        db_alias = 'logo'
    else:
        db_alias = 'default'
    return model.objects.using(db_alias)


def get_bundle_id(data):
    bundle_id = data.get('bundle_id', None)
    if not bundle_id:
        return None, "Bundle id is not found in request payload."
    if bundle_id not in settings.APP_BUNDLE_IDS:
        return None, "Provided bundle id is not valid."
    return bundle_id, ''


def clean_data(data):
    clean_items = ['user_identifier', 'bundle_id', 'campaign_id']
    for item in clean_items:
        if item in data.keys():
            del data[item]
    return data
