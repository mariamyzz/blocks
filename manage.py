#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals

import os
import sys

from server.settings.config import SETTINGS_FILE  # NOQA

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_FILE)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
