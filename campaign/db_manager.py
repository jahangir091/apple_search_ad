from django.conf import settings


def get_model_manager(model, bundle_id):
    for key, value in settings.APP_INFO.items():
        if value['bundle_id'] == bundle_id:
            db_alias = value['db_alias']
            return model.objects.using(db_alias)
    return model.objects.using('default')


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
