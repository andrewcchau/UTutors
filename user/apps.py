from django.apps import AppConfig
from django.db.models.signals import m2m_changed, post_save


class UserConfig(AppConfig):
    name = 'user'
    #
    # def ready(self):
    #     from user.signals import my_callback
    #     m2m_changed.connect(my_callback)