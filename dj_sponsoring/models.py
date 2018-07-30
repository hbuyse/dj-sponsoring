# coding=utf-8

import os

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


def sponsors_logo_upload_to(instance, filename):
    """Callback to create the path where to store the files
    The file will be uploaded to MEDIA_ROOT/sponsors/<sponsor_name>/logo<extension>
    """
    print("logo upload")
    return 'sponsors/{0}/logo{1}'.format(instance.name, os.path.splitext(filename)[1])


def sponsors_img_upload_to(instance, filename):
    """Callback to create the path where to store the files
    The file will be uploaded to MEDIA_ROOT/sponsors/<sponsor_name>/img/<filename>
    """
    return 'sponsors/{0}/img/{1}'.format(instance.sponsor.name, filename)


def sponsors_file_upload_to(instance, filename):
    """Callback to create the path where to store the files
    The file will be uploaded to MEDIA_ROOT/sponsors/<sponsor_name>/file/<filename>
    """
    return 'sponsors/{0}/file/{1}'.format(instance.sponsor.name, filename)


class Sponsor(models.Model):
    """Sponsor entry class handler"""
    name = models.CharField(_('Sponsor name'), max_length=128)
    summary = models.CharField(_('Sponsor summary'), max_length=512)
    description = MarkdownxField(_('Sponsor description'))
    logo = models.ImageField(upload_to=sponsors_logo_upload_to)
    url = models.URLField(_('Sponsor url'))
    created = models.DateTimeField('Sponsor creation date', auto_now_add=True)
    modified = models.DateTimeField('Sponsor last modification date', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Sponsor")
        verbose_name_plural = _("Sponsors")
        ordering = ("name", "-modified", "-created")

    def description_md(self):
        return markdownify(self.description)


class SponsorImage(models.Model):
    """Sponsor image class handler"""
    sponsor = models.ForeignKey('Sponsor', on_delete=models.CASCADE)
    img = models.ImageField(_('Sponsor image'), upload_to=sponsors_img_upload_to)
    alt = models.CharField(_('Sponsor image alternative text'), max_length=128)
    description = models.TextField(_('Sponsor image description text'), max_length=512, blank=True)
    created = models.DateTimeField('Sponsor image creation date', auto_now_add=True)
    modified = models.DateTimeField('Sponsor image last modification date', auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.sponsor.name, self.alt)

    class Meta:
        verbose_name = _("Sponsor photo")
        verbose_name_plural = _("Sponsor photos")
        ordering = ("sponsor", "created")


class SponsorFile(models.Model):
    """Sponsor file class handler"""
    sponsor = models.ForeignKey('Sponsor', on_delete=models.CASCADE)
    file = models.FileField(_('Sponsor file'), upload_to=sponsors_file_upload_to)
    description = models.CharField(_('Sponsor file description'), max_length=128)
    created = models.DateTimeField('Sponsor file creation date', auto_now_add=True)
    modified = models.DateTimeField('Sponsor file last modification date', auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.sponsor.name, self.description)

    class Meta:
        verbose_name = _("Sponsor file")
        verbose_name_plural = _("Sponsor files")
        ordering = ("sponsor", "created")
