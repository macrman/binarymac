from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name="Date published")
    content = models.TextField()

    def __unicode__(self):
        return self.title
