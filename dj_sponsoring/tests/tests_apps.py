#!/usr/bin/env python
# coding=utf-8

"""
test_dj-sponsoring
------------

Tests for `dj-sponsoring` apps module.
"""

from dj_sponsoring.apps import DjSponsoringConfig

from django.apps import apps


def test_apps():
    assert DjSponsoringConfig.name == 'dj_sponsoring'
    assert apps.get_app_config('dj_sponsoring').name == 'dj_sponsoring'
