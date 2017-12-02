# -*- coding: utf-8 -*-

import os

from fnmatch import fnmatch

from decouple import AutoConfig
from unipath import Path


# `unipath` is better than writing:
# BASE_DIR = dirname(dirname(dirname(dirname(__file__))))
BASE_DIR = Path(__file__).parent.parent.parent

# Defines settings file
SETTINGS = {
    True: "server.settings.dev",
    False: "server.settings.production"
}

config = AutoConfig(search_path=os.path.join(BASE_DIR, 'config'))
SETTINGS_FILE = SETTINGS[config('DEBUG', cast=bool)]
