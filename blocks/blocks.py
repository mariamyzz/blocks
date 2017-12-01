from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class PersonBlock(blocks.StructBlock):
    first_name = blocks.CharBlock(required=True)
    surname = blocks.CharBlock(required=True)
    photo = ImageChooserBlock()
    biography = blocks.RichTextBlock()

    class Meta:
        # https://github.com/wagtail/wagtail/blob/master/wagtail/contrib/styleguide/templates/wagtailstyleguide/base.html#L610
        icon = 'user'
        template='blocks/streamfield/person.html'
