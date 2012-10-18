from django.db import models
from django.template.defaultfilters import slugify

class Series(models.Model):
    series_title = models.CharField(max_length=140)

    def __unicode__(self):
        return self.series_title


class Tutorial(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=140)
    content = models.FileField(upload_to='tutorials')
    part_number = models.PositiveIntegerField(blank=True)
    series = models.ForeignKey(Series, blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        titlesuper(Tutorial, self).save(*args, **kwargs)        
        


