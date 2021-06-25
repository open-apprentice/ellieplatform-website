from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Page(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=60, unique=True)
    beg_page_content = RichTextUploadingField(default='This is the beginning or top part of your content.')
    variation_id = models.AutoField(primary_key=True)
    variation_page_content = RichTextUploadingField(
        default='This is the variation content. Make a version here and another in a different page.')
    end_page_content = RichTextUploadingField(default='This is the end or bottom part of your content.')

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    meta_description = models.TextField(max_length=160, default='meta description')

    def get_absolute_url(self):
        return reverse('page:single_page', kwargs={'slug': self.slug})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

