ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        "NAME": "arches",  # Or path to database file if using sqlite3.
        "USER": "postgres",  # Not used with sqlite3.
        "PASSWORD": "postgis",  # Not used with sqlite3.
        "HOST": "postgis",  # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "5432",  # Set to empty string for default. Not used with sqlite3.
        "POSTGIS_TEMPLATE": "template_postgis",
    }
}


ELASTICSEARCH_HTTP_PORT = 9200  # this should be in increments of 200, eg: 9400, 9600, 9800
SEARCH_BACKEND = "arches.app.search.search.SearchEngine"
# see http://elasticsearch-py.readthedocs.org/en/master/api.html#elasticsearch.Elasticsearch
ELASTICSEARCH_HOSTS = [{"host": "elasticsearch", "port": ELASTICSEARCH_HTTP_PORT}]
ELASTICSEARCH_CONNECTION_OPTIONS = {"timeout": 30}
# a prefix to append to all elasticsearch indexes, note: must be lower case
ELASTICSEARCH_PREFIX = "arches"
