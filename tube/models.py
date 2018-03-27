from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


class VideoIndexPage(Page):
    mature_content = models.BooleanField(default=False)
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('mature_content')
    ]


class VideoPage(Page):
    mature_content = models.BooleanField(default=False)
    date = models.DateField("Post date")
    # intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    @property
    def get_first_photo(self):
        return self.videos.all.first.image

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
        InlinePanel('videos', label="Videos"),
        FieldPanel('mature_content')
    ]


class VideoPageGalleryVideo(Orderable):
    page = ParentalKey(VideoPage, on_delete=models.CASCADE, related_name='videos')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    url = models.URLField('Video URL')

    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('url'),
        FieldPanel('caption'),

    ]
