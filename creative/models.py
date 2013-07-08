from django.db import models
from django.utils.text import slugify


class Idea(models.Model):
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
        if not self.pk:
            self.slug = slugify(self.title)
        super(Idea, self).save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
