# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from wagtail.wagtailcore import blocks


class HeaderDescriptionBlock(blocks.StructBlock):
    header = blocks.CharBlock(required=True)
    description = blocks.CharBlock(required=False)

    class Meta:
        icon = 'pilcrow'
        label = 'Header & description'
        template='blocks/header_description/header_description.html'