from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name="Date published")
    content = models.TextField()

    def __unicode__(self):
        return self.title
