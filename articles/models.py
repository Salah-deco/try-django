from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
    title   = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now, null=True, blank=True)

    def save(self, *args, **kwargs):
        # set something
        if self.slug in None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)