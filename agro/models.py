from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class HomeItem(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(null=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Home page"
        verbose_name_plural = "Home page"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    content = RichTextUploadingField(blank=True, default=" ")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['title']
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

class Topic(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Product"
        verbose_name_plural = "Product"

    def __str__(self):
        return self.name

class Email(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Email Form'
        verbose_name_plural = 'Email Form'

class Category(models.Model):
    topic = models.ForeignKey(Topic, related_name="topics", verbose_name="Topic")
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Image category")
    top_text = RichTextUploadingField(blank=True, default=" ", verbose_name="Top text")
    description = RichTextUploadingField(blank=True, default=" ", verbose_name="Text")
    bot_text = RichTextUploadingField(blank=True, default=" ", verbose_name="Bot text")

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name


class SliderItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    url = models.URLField(max_length=200)

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Slider"

    def __str__(self):
        return self.title

class Rewiew(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    class Meta:
        ordering = ['title']
        verbose_name = "Rewiew"
        verbose_name_plural = "Rewiew"

    def __str__(self):
        return self.title