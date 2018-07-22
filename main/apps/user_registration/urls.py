from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    
    url(r'^$', views.index, name='my_index'),
    url(r'^all_userx$', views.all_userx),
    url(r'^new_registration$', views.new_registration),
    url(r'^update$',views.update, name='show'),   # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^all_userx/(?P<id>\d+)/edit$',views.edit),
    url(r'^all_userx/(?P<id>\d+)/show$',views.show),
    url(r'^all_userx/(?P<id>\d+)/$',views.show),
    url(r'^all_userx/(?P<id>\d+)/destroy$',views.destroy),
] 