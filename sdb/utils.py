from django.db import models

# DB_MAP = {
#     ('simdb', 'lounges'): 'sdb',
#     ('people', 'directory'): 'sdb',
#     ('people', 'public_active_directory'): 'sdb',
#     ('people', 'sds_users_all'): 'sdb',
#     ('people', 'medlinks'): 'sdb',
#     ('people', 'officers'): 'sdb',
#     ('packages', 'packages'): 'sdb',
#     ('guestlist', 'guest_list'): 'sdb',
#     ('api_server', 'sds_users_all'): 'sdb',
#     ('api_server', 'sds_groups'): 'sdb',
#     ('api_server', 'sds_group_membership_cache'): 'sdb',
#     ('auth', 'sds_users_all'): 'sdb',
#     ('auth', 'sds_groups'): 'sdb',
#     ('admin', 'django_admin_log'): 'sdb',
#     ('govtracker', 'gov_fin_accounts'): 'sdb',
#     ('govtracker', 'gov_fin_subaccounts'): 'sdb',
#     ('govtracker', 'gov_fin_ledger'): 'sdb',

#     ('rooming', 'rooming_room'): 'scripts_rooming',
#     ('rooming', 'rooming_grt'): 'scripts_rooming',
#     ('rooming', 'rooming_resident'): 'scripts_rooming',
# }

# READONLY_TABLES = (
#     ('api_server', 'sds_groups'),
#     ('api_server', 'sds_users_all'),
#     ('auth', 'sds_users_all'),
#     # ('api_server', 'sds_group_membership_cache'),
# )


def get_db_for_model(model):
    if model._meta.app_label == 'sdb':
        return 'sdb'
    return 'default'


class SdbRouter(object):
    def db_for_read(self, model, **hints):
        return get_db_for_model(model)

    def db_for_write(self, model, **hints):
        db = get_db_for_model(model)
        if db == 'sdb':
            raise Exception('writes not allowed on sdb')
        return db

    def allow_relation(self, obj1, obj2, **hints):
        if get_db_for_model(obj1) == get_db_for_model(obj2):
            return True
        return False

    def allow_syncdb(self, db, model):
        if db == 'sdb' or db == 'scripts_rooming':
            return False
        else:
            return True


class SdbManager(models.Manager):
    def get_queryset(self):
        return super(SdbManager, self).get_query_set().using('sdb')


class NullableCharField(models.CharField):
    def get_db_prep_value(self, value, *args, **kwargs):
        if self.null is True and value == '':
            value = None
        return super(NullableCharField,
                     self).get_db_prep_value(value, *args, **kwargs)


class NullableTextField(models.TextField):
    def get_db_prep_value(self, value, *args, **kwargs):
        if self.null is True and value == '':
            value = None
        return super(NullableCharField,
                     self).get_db_prep_value(value, *args, **kwargs)
