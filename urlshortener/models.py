from django.conf import settings
from django.db import models

from .utils import make_short_url

MAX_URL_SIZE = settings.MAX_URL_SIZE   # shorten url 최대 길이


class TimeStampedModel(models.Model):
    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class URLMap(TimeStampedModel):
    """
    Create a short url from original_url
    Save original_url with short_url
    """

    original_url = models.URLField()
    short_url = models.CharField(max_length=MAX_URL_SIZE, unique=True)

    def __str__(self):
        return f'original_url: {self.original_url}, short_url: {self.short_url}'

    def save(self, *args, **kwargs):
        # save method 동작시 short_url 생성 후 저장.
        if not self.short_url:
            self.short_url = make_short_url(self)

        super().save(*args, **kwargs)
