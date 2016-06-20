# -*- coding:utf-8 -*-
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'antlia.users'
    verbose_name = 'Usuário'

    # def ready(self):
    #     import antlia.users.signals