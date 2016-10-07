"""This file is used to specify a base url path for our project. It is possible
that we deploy our django app not on the root url of a domain. In those cases,
the BASE_PATH environment variable should be set to that subpath appended
with a trailing /
"""
import os

from django.conf.urls import url, include

urlpatterns = [
    url(r'^%s' % os.getenv('BASE_PATH', ''), include('simdb.urls')),
]
