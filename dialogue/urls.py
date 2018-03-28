from django.conf.urls import url
from . import views

app_name = 'dialogue'

urlpatterns = [
    url(r'list/$', views.BlatListView.as_view(), name='blat_list_url'),
    url(r'list/(?P<pk>\d+)/$', views.BlatDetailView.as_view(), name='blat_detail_url'),
    url(r'list/(?P<pk>\d+)/comment/$', views.add_comment_to_blat, name='blat_comment_url'),
    url(r'list/(?P<pk>\d+)/like/$', views.dialogue_like, name='blat_likes_url'),
    url(r'search/$', views.search, name='blat_search_url'),
]
