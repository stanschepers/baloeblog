from django.db import models
from django.utils import timezone
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page


class Team(models.Model):
    name = models.CharField(max_length=63)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Voting(models.Model):
    short_name = models.CharField(max_length=15, unique=True)
    teams = models.ManyToManyField(Team)
    end = models.DateTimeField()

    @property
    def has_ended(self):
        return timezone.now() >= self.end

    @property
    def votes_per_team(self):
        output = {}
        for team in self.teams.filter(voting=self):
            try:
                q = self.votes.filter(team=team).count()
            except:
                q = -1
            output[team.name] = q
        output['finished'] = self.has_ended
        return output

    @property
    def best_name(self):
        return self.votes.order_by('votes').reverse().first().name

    @property
    def best_vote(self):
        return self.votes.order_by('votes')

    def __str__(self):
        return '%s %s' % (self.short_name, self.votes_per_team)


class Vote(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='team')
    voting = models.ForeignKey(Voting, on_delete=models.SET_NULL, null=True, related_name='votes')

    def __str__(self):
        return '%s for %s' % (self.voting, self.team)


class VotingPage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    voting = models.NullBooleanField(default=True)
    votings = models.ManyToManyField(Voting)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        FieldPanel('voting'),
        FieldPanel('votings'),
    ]
