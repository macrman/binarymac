from django.db import models


class Idea(models.Model):
    title = models.CharField(max_length=100)
    stage = models.ForeignKey('Stage')
    project = models.ManyToManyField('Project', blank=True)
    published = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True, blank=True)
    featured_image = models.ImageField(upload_to="featured", blank=True)

    def __unicode__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Stage(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="stage_icons", blank=True)

    def __unicode__(self):
        return self.name
