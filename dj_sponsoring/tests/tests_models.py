#!/usr/bin/env python
# coding=utf-8

"""
test_dj-sponsoring
------------

Tests for `dj-sponsoring` models module.
"""

from dj_sponsoring.models import Sponsor, SponsorDocument, SponsorImage, sponsors_upload_to

from django.test import TestCase


class TestSponsorModel(TestCase):

    def test_string_representation(self):
        d = {
            "name": "Toto",
            "summary": "Toto is in da place",
            "description": "# Toto",
            "url": "http://google.fr"
        }
        s = Sponsor(**d)
        self.assertEqual(str(s), "Toto")
        self.assertEqual(str(s), s.name)

    def test_verbose_name(self):
        self.assertEqual(str(Sponsor._meta.verbose_name), "sponsor")

    def test_verbose_name_plural(self):
        self.assertEqual(str(Sponsor._meta.verbose_name_plural), "sponsors")

    def test_empty_description_md(self):
        s = Sponsor()
        self.assertEqual(len(s.description_md()), 0)
        self.assertNotIn("<h1>", s.description_md())

    def test_description_md(self):
        s = Sponsor(description="# Toto")
        self.assertIn("<h1>", s.description_md())
        self.assertIn("</h1>", s.description_md())

        s = Sponsor(description="## Toto")
        self.assertIn("<h2>", s.description_md())
        self.assertIn("</h2>", s.description_md())

        s = Sponsor(description="Toto")
        self.assertIn("<p>", s.description_md())
        self.assertIn("</p>", s.description_md())

        s = Sponsor(description="*Toto*")
        self.assertIn("<em>", s.description_md())
        self.assertIn("</em>", s.description_md())

        s = Sponsor(description="**Toto**")
        self.assertIn("<strong>", s.description_md())
        self.assertIn("</strong>", s.description_md())

    def test_sponsors_logo_upload_to_cb(self):
        s = Sponsor(name="Toto")
        filename = "hello.png"
        self.assertEqual(sponsors_upload_to(s, filename), "sponsors/Toto/logo.png")
        self.assertIsNone(sponsors_upload_to(str(), filename))


class TestSponsorDocumentModel(TestCase):
    """docstring for TestSponsorModel"""

    def setUp(self):
        self.s = Sponsor.objects.create(name="Toto")

    def test_string_representation(self):
        d = {
            "sponsor": self.s,
            "description": "Toto document description",
        }
        sd = SponsorDocument(**d)
        self.assertEqual(str(sd), "{} - {}".format(sd.sponsor.name, sd.description))

    def test_verbose_name(self):
        self.assertEqual(str(SponsorDocument._meta.verbose_name), "sponsor document")

    def test_verbose_name_plural(self):
        self.assertEqual(str(SponsorDocument._meta.verbose_name_plural), "sponsor documents")

    def test_sponsors_logo_upload_to_cb(self):
        d = {
            "sponsor": self.s,
            "description": "Toto is in da place!",
        }
        sd = SponsorDocument(**d)
        filename = "hello.png"
        self.assertEqual(sponsors_upload_to(sd, filename), "sponsors/Toto/document/hello.png")


class TestSponsorImageModel(TestCase):
    """docstring for TestSponsorModel"""

    def setUp(self):
        self.s = Sponsor.objects.create(name="Toto")

    def test_string_representation(self):
        d = {
            "sponsor": self.s,
            "alt": "Toto image alternative text",
            "description": "Toto description",
        }
        s = SponsorImage(**d)
        self.assertEqual(str(s), "{} - {}".format(s.sponsor.name, s.alt))

    def test_verbose_name(self):
        self.assertEqual(str(SponsorImage._meta.verbose_name), "sponsor image")

    def test_verbose_name_plural(self):
        self.assertEqual(str(SponsorImage._meta.verbose_name_plural), "sponsor images")

    def test_empty(self):
        si = SponsorImage(sponsor=self.s)
        self.assertIsNotNone(si)

    def test_sponsors_logo_upload_to_cb(self):
        d = {
            "sponsor": self.s,
            "alt": "Toto image alternative text",
        }
        si = SponsorImage(**d)
        filename = "hello.png"
        self.assertEqual(sponsors_upload_to(si, filename), "sponsors/Toto/img/hello.png")
