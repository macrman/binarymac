from django.db import models
from django.utils.text import slugify


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
    slug = models.SlugField(blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Idea, self).save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
