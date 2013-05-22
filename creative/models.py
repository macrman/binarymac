from django.db import models


class Idea(models.Model):
    INCUBATION = 'IN'
    ANALYZATION = 'AN'
    EXPERIMENTATION = 'EX'
    DOCUMENTATION = 'DO'
    STAGE_CHOICES = (
        (INCUBATION, 'incubation'),
        (ANALYZATION, 'analyzation'),
        (EXPERIMENTATION, 'experimentation'),
        (DOCUMENTATION, 'documentation'),
    )

    stage = models.CharField(max_length=2, choices=STAGE_CHOICES,)
    title = models.CharField(max_length=100)
    project = models.ManyToManyField('Project', blank=True)
    published = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True, blank=True)
    featured_image = models.ImageField(upload_to="featured", blank=True)
    content = models.TextField()

    def __unicode__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
