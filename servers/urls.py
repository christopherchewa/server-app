from django.conf.urls import url
from servers import views

urlpatterns = [

 url(r'^$', views.server_list, name='server-list'),
 url(r'^new$', views.server_create, name='server-new'),
 url(r'^edit/(?P<pk>\d+)$', views.server_update, name='server-edit'),
 url(r'^delete/(?P<pk>\d+)$', views.server_delete, name='server-delete'),



]
