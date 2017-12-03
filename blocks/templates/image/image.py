# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class ImageBlock(blocks.StructBlock):
    photo = ImageChooserBlock(required=True)
    description = blocks.CharBlock(required=False)

    class Meta:
        icon = 'image'
        label = 'Image'
        template='image/image.html'