from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page


class Schacht(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    def __gt__(self, other):
        return self.no_votes > other.no_votes

    @property
    def no_votes(self):
        return self.votes.all().count()

    @staticmethod
    def best():
        return max(Schacht.objects.all())


class Por(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    def __gt__(self, other):
        return self.no_votes > other.no_votes

    @property
    def no_votes(self):
        return self.votes.all().count()

    @staticmethod
    def best():
        return max(Por.objects.all())


class Vote(models.Model):
    schacht = models.ForeignKey(Schacht, on_delete=models.CASCADE, related_name='votes', null=True, blank=True)
    por = models.ForeignKey(Por, on_delete=models.CASCADE, related_name='votes', null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    name = models.CharField(max_length=64, default='A', unique=True)

    def __str__(self):
        return '%s & %s by %s' % (self.schacht, self.por, self.name)


def make_table():
    output = '<table style="width:100%"> <tr> <th>Schachten</th> <th>Votes</th> <th>Porren </th> <th>Votes </th> </tr>'
    for schacht, por in list(zip(Schacht.objects.all(), Por.objects.all())):
        output += '<tr> <td> %s </td> <td> %s </td> <td> %s </td> <td> %s </td> </tr>' % (
            schacht.name, schacht.no_votes, por.name, por.no_votes)
    return output + '</table>'


class VotingPage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    plain_html = models.TextField()

    def get_context(self, request, *args, **kwargs):
        context = super(VotingPage, self).get_context(request, *args, **kwargs)
        context['schachten'] = Schacht.objects.all()
        context['porren'] = Por.objects.all()
        context['best_schacht'] = Schacht.best()
        context['best_por'] = Por.best()
        context['table'] = make_table()
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        FieldPanel('plain_html', classname="full")
    ]
