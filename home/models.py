from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList, FieldPanel, StreamFieldPanel

from blocks.blocks import QuotePersonBlock, ImageBlock


class HomePage(Page):
    body = StreamField([
        ('quoteperson', QuotePersonBlock()),
        ('image', ImageBlock()),
    ])

    common_tab = [
        FieldPanel('title'),
        StreamFieldPanel('body')
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_tab, heading='Common'),
    ])
