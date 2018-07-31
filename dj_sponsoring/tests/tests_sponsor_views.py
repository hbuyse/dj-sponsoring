#!/usr/bin/env python
# coding=utf-8

"""
test_dj-sponsoring
------------

Tests for `dj-sponsoring` models module.
"""

from dj_sponsoring.models import Sponsor, sponsors_upload_to

import pytest

pytestmark = pytest.mark.django_db


def test_string_representation():
    d = {
        "name": "Toto",
        "summary": "Toto is in da place",
        "description": "# Toto",
        "url": "http://google.fr"
    }
    s = Sponsor(**d)
    assert str(s) == "Toto"
    assert str(s) == s.name


def test_verbose_name():
    assert str(Sponsor._meta.verbose_name) == "sponsor"


def test_verbose_name_plural():
    assert str(Sponsor._meta.verbose_name_plural) == "sponsors"


def test_empty_description_md():
    s = Sponsor()
    assert len(s.description_md()) == 0
    assert "<h1>" not in s.description_md()


def test_description_md():
    s = Sponsor(description="# Toto")
    assert "<h1>" in s.description_md()
    assert "</h1>" in s.description_md()

    s = Sponsor(description="## Toto")
    assert "<h2>" in s.description_md()
    assert "</h2>" in s.description_md()

    s = Sponsor(description="Toto")
    assert "<p>" in s.description_md()
    assert "</p>" in s.description_md()

    s = Sponsor(description="*Toto*")
    assert "<em>" in s.description_md()
    assert "</em>" in s.description_md()

    s = Sponsor(description="**Toto**")
    assert "<strong>" in s.description_md()
    assert "</strong>" in s.description_md()


def test_sponsors_logo_upload_to_cb():
    s = Sponsor(name="Toto")
    filename = "hello.png"
    assert sponsors_upload_to(s, filename) == "sponsors/Toto/logo.png"
    assert sponsors_upload_to(str(), filename) is None
