from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', auth_views.login, name='accounts_login_url'),
    url(r'^signup/$', views.signup, name='accounts_signup_url'),
    url(r'^logout/$', auth_views.logout, name='accounts_logout_url'),
]
