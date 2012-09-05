from django.db import models
from django.template.defaultfilters import slugify


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=140)
    pub_date = models.DateTimeField(verbose_name="Date published")
    content = models.TextField()
    slug = models.SlugField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
