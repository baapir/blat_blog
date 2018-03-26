from django.conf.urls import url
from . import views

app_name = 'blat'

urlpatterns = [
    url(r'list/$', views.BlatListView.as_view, name='blat_list_url'),
    url(r'list/(?P<pk>\d+)/$', views.BlatDetailView.as_view, name='blat_detail_url'),
]
