# coding=utf-8

"""Filename templatetags."""

import logging
import os

from django import template

# Get an instance of a logger
logger = logging.getLogger(__name__)


register = template.Library()


@register.filter
def filename(value):
    """Return the filename of a file."""
    return os.path.basename(value.file.name)


@register.filter
def get_icon_extension(value):
    """Return the extension of a file."""
    icon = "file"
    extension = os.path.basename(value.file.name).split('.')[-1]

    tab = {
        "file-archive": ['zip', 'tar', 'gz', 'bz2'],
        "file-audio": ['ogg', 'mp3'],
        "file-code": ['py', 'c', 'cpp', 'java', 'html', 'css'],
        "file-excel": ['xls', 'xlsx'],
        "file-image": ['png', 'jpeg', 'svg'],
        "file-pdf": ['pdf'],
        "file-powerpoint": ['ppt', 'pptx'],
        "file-prescription": ['TODO'],
        "file-video": ['mkv', 'mp4'],
        "file-word": ['doc', 'docx'],
    }

    for k, v in tab.items():
        if extension in v:
            logger.info('Found extension ' + extension)
            icon = k

    return icon
