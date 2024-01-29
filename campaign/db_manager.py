from django.conf import settings


def get_model_manager(model, db_alias):
    if not db_alias:
        db_alias = 'default'
    return model.objects.using(db_alias)


def exist_db(db_alias):
    databases = settings.DATABASES
    if db_alias in databases or not db_alias:
        return True
    return False


def get_app_name_from_db_alias(db_alias):
    if db_alias == 'logo':
        return 'logo_app'
    return 'remote_app'
