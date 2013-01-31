from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    stage = models.ForeignKey('Stage')
    project = models.ManyToManyField('Project')

    def __unicode__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Stage(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
