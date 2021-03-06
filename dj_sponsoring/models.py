# coding=utf-8
"""."""

import os

from django.db import models
from django.utils.translation import ugettext_lazy as _

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

from .storage import OverwriteStorage


def sponsors_upload_to(instance, filename):
    """Callback to create the path where to store the files.

    If the file instance is a Sponsor, the file has to be the logo so it will be uploaded to
        MEDIA_ROOT/sponsors/<sponsor_name>/logo<ext>.
    If the file instance is a SponsorImage, the file has to be an image so it will be uploaded to
        MEDIA_ROOT/sponsors/<sponsor_name>/images/<filename>.
    If the file instance is a SponsorFile, the file has to be a file so it will be uploaded to
        MEDIA_ROOT/sponsors/<sponsor_name>/files/<filename>.
    """
    path = None
    if isinstance(instance, Sponsor):
        basename, ext = os.path.splitext(filename)
        path = os.path.join('sponsors', instance.name, 'logo{}'.format(ext))
    elif isinstance(instance, SponsorImage):
        path = os.path.join('sponsors', instance.sponsor.name, 'images', filename)
    elif isinstance(instance, SponsorFile):
        path = os.path.join('sponsors', instance.sponsor.name, 'files', filename)

    return path


class Sponsor(models.Model):
    """Sponsor entry class handler."""

    name = models.CharField(_('Sponsor name'), max_length=128)
    summary = models.CharField(_('Sponsor summary'), max_length=512)
    description = MarkdownxField(_('Sponsor description'))
    logo = models.ImageField(_('Sponsor logo'), storage=OverwriteStorage(), upload_to=sponsors_upload_to)
    url = models.URLField(_('Sponsor url'))
    created = models.DateTimeField('Sponsor creation date', auto_now_add=True)
    modified = models.DateTimeField('Sponsor last modification date', auto_now=True)

    def __str__(self):
        """Get name of the object."""
        return self.name

    class Meta:
        """Meta class."""

        verbose_name = _("sponsor")
        verbose_name_plural = _("sponsors")
        ordering = ("name", "-modified", "-created")

    def description_md(self):
        """Return the description text mardownified."""
        return markdownify(self.description)


class SponsorImage(models.Model):
    """Sponsor image class handler."""

    sponsor = models.ForeignKey('Sponsor', on_delete=models.CASCADE)
    img = models.ImageField(_('Sponsor image'), upload_to=sponsors_upload_to)
    alt = models.CharField(_('Sponsor image alternative text'), max_length=128)
    description = models.TextField(_('Sponsor image description text'), max_length=512, blank=True)
    created = models.DateTimeField('Sponsor image creation date', auto_now_add=True)
    modified = models.DateTimeField('Sponsor image last modification date', auto_now=True)

    def __str__(self):
        """Get name of the object."""
        return "{} - {}".format(self.sponsor.name, self.alt)

    class Meta:
        """Meta class."""

        verbose_name = _("sponsor image")
        verbose_name_plural = _("sponsor images")
        ordering = ("sponsor", "created")


class SponsorFile(models.Model):
    """Sponsor file class handler."""

    sponsor = models.ForeignKey('Sponsor', on_delete=models.CASCADE)
    file = models.FileField(_('Sponsor file'), upload_to=sponsors_upload_to)
    name = models.CharField(_('Sponsor file name'), max_length=128)
    description = models.CharField(_('Sponsor file small description'), max_length=128)
    created = models.DateTimeField('Sponsor file creation date', auto_now_add=True)
    modified = models.DateTimeField('Sponsor file last modification date', auto_now=True)

    def __str__(self):
        """Get name of the object."""
        return "{} - {}".format(self.sponsor.name, self.name)

    class Meta:
        """Meta class."""

        verbose_name = _("sponsor file")
        verbose_name_plural = _("sponsor files")
        ordering = ("sponsor", "name", "created")
