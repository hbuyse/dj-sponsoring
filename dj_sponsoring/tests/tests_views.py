#! /usr/bin/env python
# coding=utf-8

from dj_sponsoring.models import Sponsor

from django.contrib.auth.models import AnonymousUser, Group, Permission, User
from django.test import TestCase
from django.urls import reverse


class TestSponsorListView(TestCase):

    def test_sponsors_list_view_empty(self):
        r = self.client.get(reverse('dj_sponsoring:sponsor-list'))
        self.assertEqual(r.status_code, 200)
        self.assertIn("No sponsors...", str(r.content))

    def test_sponsors_list_view_one_sponsor(self):
        Sponsor.objects.create(name="Toto")
        r = self.client.get(reverse('dj_sponsoring:sponsor-detail', kwargs={'pk': 1}))
        self.assertEqual(r.status_code, 200)
        self.assertIn("Toto", str(r.content))


class TestSponsorDetailView(TestCase):

    def test_sponsors_detail_view_not_existing(self):
        r = self.client.get(reverse('dj_sponsoring:sponsor-detail', kwargs={'pk': 1}))
        self.assertEqual(r.status_code, 404)

    def test_sponsors_detail_view(self):
        Sponsor.objects.create(name="Toto")
        r = self.client.get(reverse('dj_sponsoring:sponsor-detail', kwargs={'pk': 1}))
        self.assertEqual(r.status_code, 200)
        self.assertIn("Toto", str(r.content))


class TestSponsorCreateView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="username", password="password")
        self.dict = {
            'name': 'Toto',
            'summary': 'summary',
            'description': 'description',
            'logo': 'logo',
            'url': 'http://www.google.fr'
        }
        pass

    def teardown_method(self):
        pass

    def test_sponsors_create_view_get_as_anonymous(self):
        r = self.client.get(reverse('dj_sponsoring:sponsor-create'))
        self.assertEqual(r.status_code, 302)
        self.assertIn('login/?next=/sponsors/create', r.url)

    def test_sponsors_create_view_post_as_anonymous(self):
        r = self.client.post(reverse('dj_sponsoring:sponsor-create'), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('login/?next=/sponsors/create', r.url)

    def test_sponsors_create_view_get_as_logged_with_wrong_permissions(self):
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.get(reverse('dj_sponsoring:sponsor-create'))
        self.assertEqual(r.status_code, 302)
        self.assertIn('login/?next=/sponsors/create', r.url)

    def test_sponsors_create_view_post_as_logged_with_wrong_permissions(self):
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.post(reverse('dj_sponsoring:sponsor-create'), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('login/?next=/sponsors/create', r.url)

    def test_sponsors_create_view_get_as_logged_with_right_permissions(self):
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
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))
        self.assertFalse(self.user.has_perm('dj_sponsoring.add_sponsor'))

        self.user.user_permissions.add(Permission.objects.get(name='Can add sponsor'))
        r = self.client.post(reverse('dj_sponsoring:sponsor-create'), self.dict)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(Sponsor.objects.last().name, "Toto")
