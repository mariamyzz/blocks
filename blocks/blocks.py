from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class QuotePersonBlock(blocks.StructBlock):
    quote = blocks.CharBlock(required=True)
    first_name = blocks.CharBlock(required=True)
    surname = blocks.CharBlock(required=True)
    photo = ImageChooserBlock(required=False)

    class Meta:
        icon = 'openquote'
        label = 'Personal quote'
        template='blocks/streamfield/quote_person.html'
