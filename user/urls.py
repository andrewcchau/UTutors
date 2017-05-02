from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^classes', views.classes, name='classes'),
    url(r'^subscribe/(?P<class_num>\d+)', views.subscribe, name='subscribe'),
    url(r'^request/(?P<class_num>\d+)', views.request_tutor, name='request_tutor'),
    url(r'^profile/(?P<profile_num>\d+)', views.profile, name='profile'),
    url(r'^edit_profile/(?P<profile_num>\d+)', views.update_profile, name='edit_profile'),
    url(r'^class/(?P<class_num>\d+)', views.class_profile, name='class_profile')
]