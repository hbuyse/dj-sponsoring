#! /usr/bin/env python
# coding=utf-8

"""Tests the views."""

from dj_sponsoring.models import Sponsor

from django.conf import settings
from django.contrib.auth.models import Permission, User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

import os.path


class TestSponsorListView(TestCase):
    """Tests."""

    def test_sponsors_list_view_empty(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsors-list'))
        self.assertEqual(r.status_code, 200)
        self.assertIn("No sponsors...", str(r.content))

    def test_sponsors_list_view_one_sponsor(self):
        """Tests."""
        Sponsor.objects.create(name="Toto")
        r = self.client.get(reverse('dj_sponsoring:sponsor-detail', kwargs={'pk': 1}))
        self.assertEqual(r.status_code, 200)
        self.assertIn("Toto", str(r.content))


class TestSponsorDetailView(TestCase):
    """Tests."""

    def test_sponsors_detail_view_not_existing(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-detail', kwargs={'pk': 1}))
        self.assertEqual(r.status_code, 404)

    def test_sponsors_detail_view(self):
        """Tests."""
        Sponsor.objects.create(name="Toto")
        r = self.client.get(reverse('dj_sponsoring:sponsor-detail', kwargs={'pk': 1}))
        self.assertEqual(r.status_code, 200)
        self.assertIn("Toto", str(r.content))


class TestSponsorCreateView(TestCase):
    """Tests."""

    def setUp(self):
        """Tests."""
        self.user = User.objects.create_user(username="username", password="password")
        self.dict = {
            'name': 'Toto',
            'summary': 'summary',
            'description': 'description',
            'url': 'http://www.google.fr',
            'logo': SimpleUploadedFile(name='index.png',
                                       content=open("dj_sponsoring/tests/index.png", 'rb').read(),
                                       content_type='image/png')
        }
        pass

    def teardown_method(self):
        """Tests."""
        pass

    def test_sponsors_create_view_get_as_anonymous(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-create'))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/create', r.url)

    def test_sponsors_create_view_post_as_anonymous(self):
        """Tests."""
        r = self.client.post(reverse('dj_sponsoring:sponsor-create'), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/create', r.url)

    def test_sponsors_create_view_get_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.get(reverse('dj_sponsoring:sponsor-create'))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/create', r.url)

    def test_sponsors_create_view_post_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.post(reverse('dj_sponsoring:sponsor-create'), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/create', r.url)

    def test_sponsors_create_view_get_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))
        self.assertFalse(self.user.has_perm('dj_sponsoring.add_sponsor'))

        self.user.user_permissions.add(Permission.objects.get(name='Can add sponsor'))
        r = self.client.get(reverse('dj_sponsoring:sponsor-create'))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(str(r.content).count('<label'), 5)
        self.assertEqual(str(r.content).count('</label>'), 5)
        self.assertIn('Sponsor name', str(r.content))
        self.assertIn('Sponsor summary', str(r.content))
        self.assertIn('Sponsor description', str(r.content))
        self.assertIn('Sponsor logo', str(r.content))
        self.assertIn('Sponsor url', str(r.content))

    def test_sponsors_create_view_post_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))
        self.assertFalse(self.user.has_perm('dj_sponsoring.add_sponsor'))

        self.user.user_permissions.add(Permission.objects.get(name='Can add sponsor'))
        r = self.client.post(reverse('dj_sponsoring:sponsor-create'), data=self.dict)
        s = Sponsor.objects.last()
        self.assertEqual(s.name, "Toto")
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, reverse('dj_sponsoring:sponsor-detail', kwargs={'pk': s.id}))
        self.assertTrue(os.path.isfile("{}/sponsors/{}/logo.png".format(settings.MEDIA_ROOT, s.name)))


class TestSponsorUpdateView(TestCase):
    """Tests."""

    def setUp(self):
        """Tests."""
        self.user = User.objects.create_user(username="username", password="password")
        self.dict = {
            'name': 'My Toto',
            'summary': 'My summary',
            'description': 'My description',
            'url': 'http://www.google.fr',
            'logo': SimpleUploadedFile(name='index.png',
                                       content=open("dj_sponsoring/tests/index.png", 'rb').read(),
                                       content_type='image/png')
        }
        self.sponsor = Sponsor.objects.create(**self.dict)
        pass

    def teardown_method(self):
        """Tests."""
        pass

    def test_sponsors_update_view_get_as_anonymous(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-update', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/update'.format(self.sponsor.id), r.url)

    def test_sponsors_update_view_post_as_anonymous(self):
        """Tests."""
        r = self.client.post(reverse('dj_sponsoring:sponsor-update', kwargs={'pk': self.sponsor.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/update'.format(self.sponsor.id), r.url)

    def test_sponsors_update_view_get_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.get(reverse('dj_sponsoring:sponsor-update', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/update'.format(self.sponsor.id), r.url)

    def test_sponsors_update_view_post_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.post(reverse('dj_sponsoring:sponsor-update', kwargs={'pk': self.sponsor.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/update'.format(self.sponsor.id), r.url)

    def test_sponsors_update_view_get_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))
        self.assertFalse(self.user.has_perm('dj_sponsoring.change_sponsor'))

        self.user.user_permissions.add(Permission.objects.get(name='Can change sponsor'))
        r = self.client.get(reverse('dj_sponsoring:sponsor-update', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(str(r.content).count('<label'), 5)
        self.assertEqual(str(r.content).count('</label>'), 5)
        self.assertIn('Sponsor name', str(r.content))
        self.assertIn('Toto', str(r.content))
        self.assertIn('Sponsor summary', str(r.content))
        self.assertIn('My summary', str(r.content))
        self.assertIn('Sponsor description', str(r.content))
        self.assertIn('My description', str(r.content))
        self.assertIn('Sponsor logo', str(r.content))
        self.assertIn('logo.png', str(r.content))
        self.assertIn('Sponsor url', str(r.content))
        self.assertIn('http://www.google.fr', str(r.content))

    def test_sponsors_update_view_post_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))
        self.assertFalse(self.user.has_perm('dj_sponsoring.change_sponsor'))

        self.user.user_permissions.add(Permission.objects.get(name='Can change sponsor'))
        self.dict['name'] = 'Toto new'
        self.dict['logo'] = SimpleUploadedFile(name='index.png',
                                               content=open("dj_sponsoring/tests/index.png", 'rb').read(),
                                               content_type='image/png')

        r = self.client.post(reverse('dj_sponsoring:sponsor-update', kwargs={'pk': self.sponsor.id}), data=self.dict)
        s = Sponsor.objects.get(id=self.sponsor.id)
        self.assertEqual(s.name, "Toto new")
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, reverse('dj_sponsoring:sponsor-detail', kwargs={'pk': s.id}))
        self.assertTrue(os.path.isfile("{}/sponsors/{}/logo.png".format(settings.MEDIA_ROOT, s.name)))


class TestSponsorDeleteView(TestCase):
    """Tests."""

    def setUp(self):
        """Tests."""
        self.user = User.objects.create_user(username="username", password="password")
        self.dict = {
            'name': 'My Toto',
            'summary': 'My summary',
            'description': 'My description',
            'url': 'http://www.google.fr',
            'logo': SimpleUploadedFile(name='index.png',
                                       content=open("dj_sponsoring/tests/index.png", 'rb').read(),
                                       content_type='image/png')
        }
        self.sponsor = Sponsor.objects.create(**self.dict)
        pass

    def teardown_method(self):
        """Tests."""
        pass

    def test_sponsors_delete_view_get_as_anonymous(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-delete', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/delete'.format(self.sponsor.id), r.url)

    def test_sponsors_delete_view_post_as_anonymous(self):
        """Tests."""
        r = self.client.post(reverse('dj_sponsoring:sponsor-delete', kwargs={'pk': self.sponsor.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/delete'.format(self.sponsor.id), r.url)

    def test_sponsors_delete_view_get_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.get(reverse('dj_sponsoring:sponsor-delete', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/delete'.format(self.sponsor.id), r.url)

    def test_sponsors_delete_view_post_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.post(reverse('dj_sponsoring:sponsor-delete', kwargs={'pk': self.sponsor.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/delete'.format(self.sponsor.id), r.url)

    def test_sponsors_delete_view_get_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))
        self.assertFalse(self.user.has_perm('dj_sponsoring.delete_sponsor'))

        self.user.user_permissions.add(Permission.objects.get(name='Can delete sponsor'))
        r = self.client.get(reverse('dj_sponsoring:sponsor-delete', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 200)
        self.assertIn("<h1 class=\"float-left\">{}</h1>".format(self.sponsor.name), str(r.content))
        self.assertIn("<p>Do you really want to delete that sponsor?</p>", str(r.content))

    def test_sponsors_delete_view_post_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))
        self.assertFalse(self.user.has_perm('dj_sponsoring.delete_sponsor'))

        self.user.user_permissions.add(Permission.objects.get(name='Can delete sponsor'))
        self.assertEqual(Sponsor.objects.count(), 1)
        r = self.client.post(reverse('dj_sponsoring:sponsor-delete', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(Sponsor.objects.count(), 0)
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, reverse('dj_sponsoring:sponsors-list'))
