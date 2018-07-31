#!/usr/bin/env python
# coding=utf-8

"""
test_dj-sponsoring
------------

Tests for `dj-sponsoring` models module.
"""

from dj_sponsoring.models import Sponsor, SponsorImage, sponsors_upload_to

import pytest

pytestmark = pytest.mark.django_db


@pytest.fixture
def sponsor():
    return Sponsor(name="Toto")


def test_string_representation(sponsor):
    d = {
        "sponsor": sponsor,
        "alt": "Toto image alternative text",
        "description": "Toto description",
    }
    s = SponsorImage(**d)
    assert str(s) == "{} - {}".format(s.sponsor.name, s.alt)


def test_verbose_name():
    assert str(SponsorImage._meta.verbose_name) == "sponsor image"


def test_verbose_name_plural():
    assert str(SponsorImage._meta.verbose_name_plural) == "sponsor images"


def test_empty(sponsor):
    si = SponsorImage(sponsor=sponsor)
    assert si is not None


def test_sponsors_logo_upload_to_cb(sponsor):
    d = {
        "sponsor": sponsor,
        "alt": "Toto image alternative text",
    }
    si = SponsorImage(**d)
    filename = "hello.png"
    assert sponsors_upload_to(si, filename) == "sponsors/Toto/img/hello.png"
