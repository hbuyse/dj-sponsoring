# coding=utf-8

"""Admin."""

from django.contrib import admin

from .models import (
    Sponsor,
    SponsorFile,
    SponsorImage,
)


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'url',
        'created',
        'modified',
    )
    date_hierarchy = 'created'


@admin.register(SponsorFile)
class SponsorFileAdmin(admin.ModelAdmin):
    list_display = (
        'sponsor',
        'name',
        'created',
        'modified',
    )
    date_hierarchy = 'created'


@admin.register(SponsorImage)
class SponsorImageAdmin(admin.ModelAdmin):
    list_display = (
        'sponsor',
        'alt',
        'created',
        'modified',
    )
    date_hierarchy = 'created'
