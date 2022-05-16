from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

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
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)

# This is sent at the beginning of a model’s save() method.
def article_pre_save(sender, instance, *args, **kwargs):
    print('--> pre_save')
    instance.slug = slugify(instance.title)

pre_save.connect(article_pre_save, sender=Article)

#Like pre_save, but sent at the end of the save() method.
def article_post_save(sender, instance, created, *args, **kwargs):
    print('--> post_save : ', end=' ')
    if created:
        print("Article created")
    else:
        print("Article not created")
pre_save.connect(article_post_save, sender=Article)