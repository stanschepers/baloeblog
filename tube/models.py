from django.db import models

# Create your models here.
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtailmedia.edit_handlers import MediaChooserPanel


class BlogPageWithMedia(Page):
    text = RichTextField(blank=False)
    media = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('text'),
        MediaChooserPanel('media'),
    ]