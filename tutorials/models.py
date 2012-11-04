import os

from django.db import models
from django.template.defaultfilters import slugify
from binarymac.settings import MEDIA_ROOT


class Tutorial(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField()
    path = models.FilePathField(path=os.path.join(MEDIA_ROOT, "tutorials"), recursive=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        titlesuper(Tutorial, self).save(*args, **kwargs)        
