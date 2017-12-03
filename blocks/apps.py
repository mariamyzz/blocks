# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
import os, sys

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_TO_BLOCKS = os.path.join(PATH, 'templates')

class BlocksConfig(AppConfig):
    name = 'blocks'
        