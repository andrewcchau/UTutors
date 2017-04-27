from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^classes', views.classes, name='classes'),
    url(r'^profile/(?P<profile_num>\d+)', views.update_profile, name='profile')
]