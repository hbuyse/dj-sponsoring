#! /usr/bin/env python
# coding=utf-8

"""Tests the views."""

from dj_sponsoring.models import Sponsor, SponsorImage, SponsorFile

from django.conf import settings
from django.contrib.auth.models import Permission, User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

import os.path


class TestSponsorListView(TestCase):
    """Tests."""

    def setUp(self):
        """Tests."""
        self.dict = {
            'name': 'Toto',
            'summary': 'summary',
            'description': 'description',
            'url': 'http://www.google.fr',
            'logo': SimpleUploadedFile(name='index.png',
                                       content=open("dj_sponsoring/tests/index.png", 'rb').read(),
                                       content_type='image/png')
        }

    def test_sponsors_list_view_empty(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsors-list'))
        self.assertEqual(r.status_code, 200)
        self.assertIn("No sponsors...", str(r.content))

    def test_sponsors_list_view_one_sponsor(self):
        """Tests."""
        Sponsor.objects.create(**self.dict)
        r = self.client.get(reverse('dj_sponsoring:sponsors-list'))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(str(r.content).count('<ul>'), 1)
        self.assertEqual(str(r.content).count('<li>'), 1)
        self.assertIn("Toto", str(r.content))
        self.assertEqual(str(r.content).count('</li>'), 1)
        self.assertEqual(str(r.content).count('</ul>'), 1)


class TestSponsorDetailView(TestCase):
    """Tests."""

    def test_sponsor_detail_view_not_existing(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-detail', kwargs={'pk': 1}))
        self.assertEqual(r.status_code, 404)

    def test_sponsor_detail_view(self):
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

    def test_sponsor_create_view_get_as_anonymous(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-create'))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/create', r.url)

    def test_sponsor_create_view_post_as_anonymous(self):
        """Tests."""
        r = self.client.post(reverse('dj_sponsoring:sponsor-create'), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/create', r.url)

    def test_sponsor_create_view_get_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.get(reverse('dj_sponsoring:sponsor-create'))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/create', r.url)

    def test_sponsor_create_view_post_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.post(reverse('dj_sponsoring:sponsor-create'), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/create', r.url)

    def test_sponsor_create_view_get_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

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

    def test_sponsor_create_view_post_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

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

    def test_sponsor_update_view_get_as_anonymous(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-update', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/update'.format(self.sponsor.id), r.url)

    def test_sponsor_update_view_post_as_anonymous(self):
        """Tests."""
        r = self.client.post(reverse('dj_sponsoring:sponsor-update', kwargs={'pk': self.sponsor.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/update'.format(self.sponsor.id), r.url)

    def test_sponsor_update_view_get_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.get(reverse('dj_sponsoring:sponsor-update', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/update'.format(self.sponsor.id), r.url)

    def test_sponsor_update_view_post_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.post(reverse('dj_sponsoring:sponsor-update', kwargs={'pk': self.sponsor.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/update'.format(self.sponsor.id), r.url)

    def test_sponsor_update_view_get_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

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

    def test_sponsor_update_view_post_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

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

    def test_sponsor_delete_view_get_as_anonymous(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-delete', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/delete'.format(self.sponsor.id), r.url)

    def test_sponsor_delete_view_post_as_anonymous(self):
        """Tests."""
        r = self.client.post(reverse('dj_sponsoring:sponsor-delete', kwargs={'pk': self.sponsor.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/delete'.format(self.sponsor.id), r.url)

    def test_sponsor_delete_view_get_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.get(reverse('dj_sponsoring:sponsor-delete', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/delete'.format(self.sponsor.id), r.url)

    def test_sponsor_delete_view_post_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.post(reverse('dj_sponsoring:sponsor-delete', kwargs={'pk': self.sponsor.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/delete'.format(self.sponsor.id), r.url)

    def test_sponsor_delete_view_get_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        self.user.user_permissions.add(Permission.objects.get(name='Can delete sponsor'))
        r = self.client.get(reverse('dj_sponsoring:sponsor-delete', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 200)
        self.assertIn("<h1 class=\"float-left\">{}</h1>".format(self.sponsor.name), str(r.content))
        self.assertIn("<p>Do you really want to delete that sponsor and everything linked to it?</p>", str(r.content))

    def test_sponsor_delete_view_post_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        self.user.user_permissions.add(Permission.objects.get(name='Can delete sponsor'))
        self.assertEqual(Sponsor.objects.count(), 1)
        r = self.client.post(reverse('dj_sponsoring:sponsor-delete', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(Sponsor.objects.count(), 0)
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, reverse('dj_sponsoring:sponsors-list'))


class TestSponsorImageListView(TestCase):
    """Tests."""

    def setUp(self):
        """Setup for TestSponsorImageListView."""
        self.sponsor = Sponsor.objects.create(name="Toto")

    def test_sponsor_images_list_view_empty(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-images-list', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 200)
        self.assertIn("No images for this sponsor...", str(r.content))

    def test_sponsor_image_list_view_one_image(self):
        """Tests."""
        SponsorImage.objects.create(sponsor=self.sponsor, alt="Toto")
        r = self.client.get(reverse('dj_sponsoring:sponsor-images-list', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 200)
        self.assertIn("Toto", str(r.content))


class TestSponsorImageDetailView(TestCase):
    """Tests."""

    def setUp(self):
        """Setup for TestSponsorImageListView."""
        self.sponsor = Sponsor.objects.create(name="Toto")

    def test_sponsor_image_detail_view_not_existing(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-image-detail', kwargs={'pk': 1}))
        self.assertEqual(r.status_code, 404)

    def test_sponsor_image_detail_view(self):
        """Tests."""
        SponsorImage.objects.create(sponsor=self.sponsor, alt="My alternative text")
        r = self.client.get(reverse('dj_sponsoring:sponsor-image-detail', kwargs={'pk': 1}))
        self.assertEqual(r.status_code, 200)
        self.assertIn("Toto", str(r.content))


class TestSponsorImageCreateView(TestCase):
    """Tests."""

    def setUp(self):
        """Tests."""
        self.user = User.objects.create_user(username="username", password="password")
        self.sponsor = Sponsor.objects.create(name="Toto")
        self.dict = {
            'img': SimpleUploadedFile(name='index.png',
                                      content=open("dj_sponsoring/tests/index.png", 'rb').read(),
                                      content_type='image/png'),
            'alt': "My alt",
            'description': "My description"
        }

    def test_sponsor_image_create_view_get_as_anonymous(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-image-create', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/images/create'.format(self.sponsor.id), r.url)

    def test_sponsor_image_create_view_post_as_anonymous(self):
        """Tests."""
        r = self.client.post(reverse('dj_sponsoring:sponsor-image-create', kwargs={'pk': self.sponsor.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/images/create'.format(self.sponsor.id), r.url)

    def test_sponsor_image_create_view_get_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.get(reverse('dj_sponsoring:sponsor-image-create', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/images/create'.format(self.sponsor.id), r.url)

    def test_sponsor_image_create_view_post_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.post(reverse('dj_sponsoring:sponsor-image-create', kwargs={'pk': self.sponsor.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/images/create'.format(self.sponsor.id), r.url)

    def test_sponsor_image_create_view_get_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        self.user.user_permissions.add(Permission.objects.get(name='Can add sponsor image'))
        r = self.client.get(reverse('dj_sponsoring:sponsor-image-create', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(str(r.content).count('<label'), 3)
        self.assertEqual(str(r.content).count('</label>'), 3)
        self.assertIn('Sponsor image alternative text', str(r.content))
        self.assertIn('Sponsor image', str(r.content))
        self.assertIn('Sponsor image description text', str(r.content))

    def test_sponsor_image_create_view_post_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        self.user.user_permissions.add(Permission.objects.get(name='Can add sponsor image'))
        r = self.client.post(reverse('dj_sponsoring:sponsor-image-create',
                                     kwargs={'pk': self.sponsor.id}), data=self.dict)
        s = SponsorImage.objects.last()
        self.assertEqual(s.alt, "My alt")
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, reverse('dj_sponsoring:sponsor-image-detail', kwargs={'pk': s.id}))
        self.assertTrue(os.path.isfile(
            "{}/sponsors/{}/images/{}".format(settings.MEDIA_ROOT, s.sponsor.name, self.dict['img'].name)))


class TestSponsorImageUpdateView(TestCase):
    """Tests."""

    def setUp(self):
        """Tests."""
        self.user = User.objects.create_user(username="username", password="password")
        sponsor = Sponsor.objects.create(name="Toto")
        self.dict = {
            'sponsor': sponsor,
            'img': SimpleUploadedFile(name='index.png',
                                      content=open("dj_sponsoring/tests/index.png", 'rb').read(),
                                      content_type='image/png'),
            'alt': "My alt",
            'description': "My description"
        }
        self.si = SponsorImage.objects.create(**self.dict)

    def test_sponsor_image_update_view_get_as_anonymous(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-image-update', kwargs={'pk': self.si.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/images/{}/update'.format(self.si.id), r.url)

    def test_sponsor_image_update_view_post_as_anonymous(self):
        """Tests."""
        r = self.client.post(reverse('dj_sponsoring:sponsor-image-update', kwargs={'pk': self.si.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/images/{}/update'.format(self.si.id), r.url)

    def test_sponsor_image_update_view_get_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.get(reverse('dj_sponsoring:sponsor-image-update', kwargs={'pk': self.si.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/images/{}/update'.format(self.si.id), r.url)

    def test_sponsor_image_update_view_post_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.post(reverse('dj_sponsoring:sponsor-image-update', kwargs={'pk': self.si.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/images/{}/update'.format(self.si.id), r.url)

    def test_sponsor_image_update_view_get_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        self.user.user_permissions.add(Permission.objects.get(name='Can change sponsor image'))
        r = self.client.get(reverse('dj_sponsoring:sponsor-image-update', kwargs={'pk': self.si.id}))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(str(r.content).count('<label'), 3)
        self.assertEqual(str(r.content).count('</label>'), 3)
        self.assertIn('Sponsor image alternative text', str(r.content))
        self.assertIn('My alt', str(r.content))
        self.assertIn('Sponsor image', str(r.content))
        self.assertIn(self.si.img.name, str(r.content))
        self.assertIn('Sponsor image description', str(r.content))
        self.assertIn('My description', str(r.content))

    def test_sponsor_image_update_view_post_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        self.user.user_permissions.add(Permission.objects.get(name='Can change sponsor image'))
        self.dict['alt'] = 'My new alternative text'
        self.dict['img'] = SimpleUploadedFile(name='index.png',
                                              content=open("dj_sponsoring/tests/index.png", 'rb').read(),
                                              content_type='image/png')

        r = self.client.post(reverse('dj_sponsoring:sponsor-image-update',
                                     kwargs={'pk': self.si.id}), data=self.dict)
        si = SponsorImage.objects.get(id=self.si.id)
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, reverse('dj_sponsoring:sponsor-image-detail', kwargs={'pk': si.id}))
        self.assertEqual(si.alt, 'My new alternative text')
        self.assertTrue(os.path.isfile("{}/{}".format(settings.MEDIA_ROOT, si.img.name)))


class TestSponsorImageDeleteView(TestCase):
    """Tests."""

    def setUp(self):
        """Tests."""
        self.user = User.objects.create_user(username="username", password="password")
        sponsor = Sponsor.objects.create(name="Toto")
        self.dict = {
            'sponsor': sponsor,
            'img': SimpleUploadedFile(name='index.png',
                                      content=open("dj_sponsoring/tests/index.png", 'rb').read(),
                                      content_type='image/png'),
            'alt': "My alt",
            'description': "My description"
        }
        self.si = SponsorImage.objects.create(**self.dict)

    def test_sponsor_image_delete_view_get_as_anonymous(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-image-delete', kwargs={'pk': self.si.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/images/{}/delete'.format(self.si.id), r.url)

    def test_sponsor_image_delete_view_post_as_anonymous(self):
        """Tests."""
        r = self.client.post(reverse('dj_sponsoring:sponsor-image-delete', kwargs={'pk': self.si.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/images/{}/delete'.format(self.si.id), r.url)

    def test_sponsor_image_delete_view_get_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.get(reverse('dj_sponsoring:sponsor-image-delete', kwargs={'pk': self.si.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/images/{}/delete'.format(self.si.id), r.url)

    def test_sponsor_image_delete_view_post_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.post(reverse('dj_sponsoring:sponsor-image-delete', kwargs={'pk': self.si.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/images/{}/delete'.format(self.si.id), r.url)

    def test_sponsor_image_delete_view_get_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        self.user.user_permissions.add(Permission.objects.get(name='Can delete sponsor image'))
        r = self.client.get(reverse('dj_sponsoring:sponsor-image-delete', kwargs={'pk': self.si.id}))
        self.assertEqual(r.status_code, 200)
        self.assertIn("<h1 class=\"float-left\">{}</h1>".format(self.si), str(r.content))
        self.assertIn("<p>Do you really want to delete that image?</p>", str(r.content))

    def test_sponsor_image_delete_view_post_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        self.user.user_permissions.add(Permission.objects.get(name='Can delete sponsor image'))
        self.assertEqual(SponsorImage.objects.count(), 1)
        r = self.client.post(reverse('dj_sponsoring:sponsor-image-delete', kwargs={'pk': self.si.id}))
        self.assertEqual(SponsorImage.objects.count(), 0)
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, reverse('dj_sponsoring:sponsor-images-list', kwargs={'pk': self.si.sponsor.id}))


class TestSponsorFileListView(TestCase):
    """Tests."""

    def setUp(self):
        """Setup for TestSponsorImageListView."""
        self.sponsor = Sponsor.objects.create(name="Toto")

    def test_sponsor_images_list_view_empty(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-files-list', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 200)
        self.assertIn("No files for this sponsor...", str(r.content))

    def test_sponsor_image_list_view_one_image(self):
        """Tests."""
        SponsorFile.objects.create(sponsor=self.sponsor, name="My name", description="My description")
        r = self.client.get(reverse('dj_sponsoring:sponsor-files-list', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 200)
        self.assertIn(">My name</a>", str(r.content))


class TestSponsorFileDetailView(TestCase):
    """Tests."""

    def setUp(self):
        """Setup for TestSponsorImageListView."""
        self.sponsor = Sponsor.objects.create(name="Toto")

    def test_sponsor_file_detail_view_not_existing(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-file-detail', kwargs={'pk': 1}))
        self.assertEqual(r.status_code, 404)

    def test_sponsor_file_detail_view(self):
        """Tests."""
        SponsorFile.objects.create(sponsor=self.sponsor, name="My name", description="My description")
        r = self.client.get(reverse('dj_sponsoring:sponsor-file-detail', kwargs={'pk': 1}))
        self.assertEqual(r.status_code, 200)
        self.assertIn("Toto", str(r.content))


class TestSponsorFileCreateView(TestCase):
    """Tests."""

    def setUp(self):
        """Tests."""
        self.user = User.objects.create_user(username="username", password="password")
        self.sponsor = Sponsor.objects.create(name="Toto")
        self.dict = {
            'file': SimpleUploadedFile(name='file.txt',
                                       content=open("dj_sponsoring/tests/file.txt", 'rb').read(),
                                       content_type='text/plain'),
            'name': "My name",
            'description': "My description"
        }

    def test_sponsor_file_create_view_get_as_anonymous(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-file-create', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/files/create'.format(self.sponsor.id), r.url)

    def test_sponsor_file_create_view_post_as_anonymous(self):
        """Tests."""
        r = self.client.post(reverse('dj_sponsoring:sponsor-file-create', kwargs={'pk': self.sponsor.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/files/create'.format(self.sponsor.id), r.url)

    def test_sponsor_file_create_view_get_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.get(reverse('dj_sponsoring:sponsor-file-create', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/files/create'.format(self.sponsor.id), r.url)

    def test_sponsor_file_create_view_post_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.post(reverse('dj_sponsoring:sponsor-file-create', kwargs={'pk': self.sponsor.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/{}/files/create'.format(self.sponsor.id), r.url)

    def test_sponsor_file_create_view_get_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        self.user.user_permissions.add(Permission.objects.get(name='Can add sponsor file'))
        r = self.client.get(reverse('dj_sponsoring:sponsor-file-create', kwargs={'pk': self.sponsor.id}))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(str(r.content).count('<label'), 3)
        self.assertEqual(str(r.content).count('</label>'), 3)
        self.assertIn('Sponsor file name', str(r.content))
        self.assertIn('Sponsor file', str(r.content))
        self.assertIn('Sponsor file small description', str(r.content))

    def test_sponsor_file_create_view_post_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        self.user.user_permissions.add(Permission.objects.get(name='Can add sponsor file'))
        r = self.client.post(reverse('dj_sponsoring:sponsor-file-create',
                                     kwargs={'pk': self.sponsor.id}), data=self.dict)
        s = SponsorFile.objects.last()
        self.assertEqual(s.name, "My name")
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, reverse('dj_sponsoring:sponsor-file-detail', kwargs={'pk': s.id}))
        self.assertTrue(os.path.isfile(
            "{}/sponsors/{}/files/{}".format(settings.MEDIA_ROOT, s.sponsor.name, self.dict['file'].name)))


class TestSponsorFileUpdateView(TestCase):
    """Tests."""

    def setUp(self):
        """Tests."""
        self.user = User.objects.create_user(username="username", password="password")
        sponsor = Sponsor.objects.create(name="Toto")
        self.dict = {
            'sponsor': sponsor,
            'file': SimpleUploadedFile(name='file.txt',
                                       content=open("dj_sponsoring/tests/file.txt", 'rb').read(),
                                       content_type='text/plain'),
            'name': "My name",
            'description': "My description"
        }
        self.sf = SponsorFile.objects.create(**self.dict)

    def test_sponsor_file_update_view_get_as_anonymous(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-file-update', kwargs={'pk': self.sf.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/files/{}/update'.format(self.sf.id), r.url)

    def test_sponsor_file_update_view_post_as_anonymous(self):
        """Tests."""
        r = self.client.post(reverse('dj_sponsoring:sponsor-file-update', kwargs={'pk': self.sf.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/files/{}/update'.format(self.sf.id), r.url)

    def test_sponsor_file_update_view_get_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.get(reverse('dj_sponsoring:sponsor-file-update', kwargs={'pk': self.sf.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/files/{}/update'.format(self.sf.id), r.url)

    def test_sponsor_file_update_view_post_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.post(reverse('dj_sponsoring:sponsor-file-update', kwargs={'pk': self.sf.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/files/{}/update'.format(self.sf.id), r.url)

    def test_sponsor_file_update_view_get_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        self.user.user_permissions.add(Permission.objects.get(name='Can change sponsor file'))
        r = self.client.get(reverse('dj_sponsoring:sponsor-file-update', kwargs={'pk': self.sf.id}))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(str(r.content).count('<label'), 3)
        self.assertEqual(str(r.content).count('</label>'), 3)
        self.assertIn('Sponsor file name', str(r.content))
        self.assertIn('My name', str(r.content))
        self.assertIn('Sponsor file', str(r.content))
        self.assertIn(self.sf.file.name, str(r.content))
        self.assertIn('Sponsor file small description', str(r.content))
        self.assertIn('My description', str(r.content))

    def test_sponsor_file_update_view_post_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        self.user.user_permissions.add(Permission.objects.get(name='Can change sponsor file'))
        self.dict['name'] = 'My new name'
        self.dict['file'] = SimpleUploadedFile(name='file.txt',
                                               content=open("dj_sponsoring/tests/file.txt", 'rb').read(),
                                               content_type='text/plain'),

        r = self.client.post(reverse('dj_sponsoring:sponsor-file-update',
                                     kwargs={'pk': self.sf.id}), data=self.dict)
        sf = SponsorFile.objects.get(id=self.sf.id)
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, reverse('dj_sponsoring:sponsor-file-detail', kwargs={'pk': sf.id}))
        self.assertEqual(sf.name, 'My new name')
        self.assertTrue(os.path.isfile("{}/{}".format(settings.MEDIA_ROOT, sf.file.name)))


class TestSponsorFileDeleteView(TestCase):
    """Tests."""

    def setUp(self):
        """Tests."""
        self.user = User.objects.create_user(username="username", password="password")
        sponsor = Sponsor.objects.create(name="Toto")
        self.dict = {
            'sponsor': sponsor,
            'file': SimpleUploadedFile(name='file.txt',
                                       content=open("dj_sponsoring/tests/file.txt", 'rb').read(),
                                       content_type='text/plain'),
            'name': "My name",
            'description': "My description"
        }
        self.sf = SponsorFile.objects.create(**self.dict)

    def test_sponsor_file_delete_view_get_as_anonymous(self):
        """Tests."""
        r = self.client.get(reverse('dj_sponsoring:sponsor-file-delete', kwargs={'pk': self.sf.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/files/{}/delete'.format(self.sf.id), r.url)

    def test_sponsor_file_delete_view_post_as_anonymous(self):
        """Tests."""
        r = self.client.post(reverse('dj_sponsoring:sponsor-file-delete', kwargs={'pk': self.sf.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/files/{}/delete'.format(self.sf.id), r.url)

    def test_sponsor_file_delete_view_get_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.get(reverse('dj_sponsoring:sponsor-file-delete', kwargs={'pk': self.sf.id}))
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/files/{}/delete'.format(self.sf.id), r.url)

    def test_sponsor_file_delete_view_post_as_logged_with_wrong_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        r = self.client.post(reverse('dj_sponsoring:sponsor-file-delete', kwargs={'pk': self.sf.id}), self.dict)
        self.assertEqual(r.status_code, 302)
        self.assertIn('?next=/files/{}/delete'.format(self.sf.id), r.url)

    def test_sponsor_file_delete_view_get_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        self.user.user_permissions.add(Permission.objects.get(name='Can delete sponsor file'))
        r = self.client.get(reverse('dj_sponsoring:sponsor-file-delete', kwargs={'pk': self.sf.id}))
        self.assertEqual(r.status_code, 200)
        self.assertIn("<h1 class=\"float-left\">{}</h1>".format(self.sf), str(r.content))
        self.assertIn("<p>Do you really want to delete that file?</p>", str(r.content))

    def test_sponsor_file_delete_view_post_as_logged_with_right_permissions(self):
        """Tests."""
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.client.login(username="username", password="password"))

        self.user.user_permissions.add(Permission.objects.get(name='Can delete sponsor file'))
        self.assertEqual(SponsorFile.objects.count(), 1)
        r = self.client.post(reverse('dj_sponsoring:sponsor-file-delete', kwargs={'pk': self.sf.id}))
        self.assertEqual(SponsorFile.objects.count(), 0)
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, reverse('dj_sponsoring:sponsor-files-list', kwargs={'pk': self.sf.sponsor.id}))
