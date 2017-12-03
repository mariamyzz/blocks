# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

class BlocksConfig(AppConfig):
    name = 'blocks'

    def ready(self):
        print('Blocks collection added.\n')
        