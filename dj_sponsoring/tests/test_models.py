#!/usr/bin/env python
# coding=utf-8

"""
test_dj-sponsoring
------------

Tests for `dj-sponsoring` models module.
"""

from django.test import TestCase

from dj_sponsoring.models import Sponsor, SponsorImage, SponsorFile


class TestSponsor(TestCase):

    def setUp(self):
        pass

    def test_empty_sponsor(self):
        s = Sponsor.objects.create()
        assert s != None

    def test_empty_sponsor2(self):
        s = Sponsor.objects.create()
        assert s != None

    def tearDown(self):
        pass
