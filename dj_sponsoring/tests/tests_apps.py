#!/usr/bin/env python
# coding=utf-8

"""
test_dj-sponsoring
------------

Tests for `dj-sponsoring` apps module.
"""

from dj_sponsoring.apps import DjSponsoringConfig

from django.apps import apps
from django.test import TestCase


class TestApps(TestCase):

    def test_apps(self):
        self.assertEqual(DjSponsoringConfig.name, 'dj_sponsoring')
        self.assertEqual(apps.get_app_config('dj_sponsoring').name, 'dj_sponsoring')
