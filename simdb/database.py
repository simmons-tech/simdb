import os

from django.conf import settings


engines = {
    'sqlite': 'django.db.backends.sqlite3',
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    'mysql': 'django.db.backends.mysql',
}


def config(service_name = 'DEFAULT'):
    engine = engines.get(os.getenv('{}_DATABASE_ENGINE'.format(service_name)), engines['sqlite'])
    name = os.getenv('{}_DATABASE_NAME'.format(service_name))
    if not name and engine == engines['sqlite']:
        name = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    return {
        'ENGINE': engine,
        'NAME': name,
        'USER': os.getenv('{}_DATABASE_USER'.format(service_name)),
        'PASSWORD': os.getenv('{}_DATABASE_PASSWORD'.format(service_name)),
        'HOST': os.getenv('{}_DATABASE_HOST'.format(service_name)),
        'PORT': os.getenv('{}_DATABASE_PORT'.format(service_name)),
    }
