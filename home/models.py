from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList, FieldPanel, StreamFieldPanel

from blocks.models import QuotePersonBlock, ImageBlock, HeaderDescriptionBlock # NOQA


class HomePage(Page):
    body = StreamField([
        ('QuotePerson', QuotePersonBlock()),
        ('Image', ImageBlock()),
        ('HeaderDescription', HeaderDescriptionBlock())
    ], blank=True)

    common_tab = [
        FieldPanel('title'),
        StreamFieldPanel('body')
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_tab, heading='Common'),
    ])
