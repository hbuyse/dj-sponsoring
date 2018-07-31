#!/usr/bin/env python
# coding=utf-8

"""
test_dj-sponsoring
------------

Tests for `dj-sponsoring` models module.
"""

from dj_sponsoring.models import Sponsor, SponsorDocument, sponsors_upload_to

import pytest

pytestmark = pytest.mark.django_db


@pytest.fixture
def sponsor():
    return Sponsor.objects.create(name="Toto")


def test_string_representation(sponsor):
    d = {
        "sponsor": sponsor,
        "description": "Toto document description",
    }
    s = SponsorDocument(**d)
    assert str(s) == "{} - {}".format(s.sponsor.name, s.description)


def test_verbose_name():
    assert str(SponsorDocument._meta.verbose_name) == "sponsor document"


def test_verbose_name_plural():
    assert str(SponsorDocument._meta.verbose_name_plural) == "sponsor documents"


def test_sponsors_logo_upload_to_cb(sponsor):
    d = {
        "sponsor": sponsor,
        "description": "Toto is in da place!",
    }
    sd = SponsorDocument(**d)
    filename = "hello.png"
    assert sponsors_upload_to(sd, filename) == "sponsors/Toto/document/hello.png"
