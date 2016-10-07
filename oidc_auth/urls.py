from django.conf.urls import url

import oidc_auth.views

urlpatterns = [
    url(r'^login/$', oidc_auth.views.login_begin, name='oidc-login'),
    url(r'^complete/$', oidc_auth.views.login_complete, name='oidc-complete'),
]
