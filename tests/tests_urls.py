#!/usr/bin/env python
# coding=utf-8

"""Tests for `dj-sponsoring` urls module."""

from django.test import TestCase
from django.urls import reverse


class TestUrlsSponsor(TestCase):
    """Tests the urls for the dj-sponsoring."""

    def test_sponsor_list_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsors-list')
        self.assertEqual(url, '/')

    def test_sponsor_create_url(self):
        """Test the URL of that allows the creation of a sponsor."""
        url = reverse('dj_sponsoring:sponsor-create')
        self.assertEqual(url, '/create')

    def test_sponsor_detail_url(self):
        """Test the URL that gives the details of a sponsor."""
        url = reverse('dj_sponsoring:sponsor-detail', kwargs={'pk': 1})
        self.assertEqual(url, '/1')

    def test_sponsor_update_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-update', kwargs={'pk': 1})
        self.assertEqual(url, "/1/update")

    def test_sponsor_delete_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-delete', kwargs={'pk': 1})
        self.assertEqual(url, "/1/delete")


class TestUrlsSponsorImage(TestCase):
    """Tests the urls for the dj-sponsoring."""

    def test_sponsor_list_images_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-images-list', kwargs={'pk': 1})
        self.assertEqual(url, "/1/images")

    def test_sponsor_image_create_url(self):
        """Test the URL that adds a image to a specific sponsor."""
        url = reverse('dj_sponsoring:sponsor-image-create', kwargs={'pk': 1})
        self.assertEqual(url, '/1/images/create')

    def test_sponsor_image_detail_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-image-detail', kwargs={'pk': 1})
        self.assertEqual(url, '/images/1')

    def test_sponsor_image_update_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-image-update', kwargs={'pk': 1})
        self.assertEqual(url, "/images/1/update")

    def test_sponsor_image_delete_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-image-delete', kwargs={'pk': 1})
        self.assertEqual(url, "/images/1/delete")


class TestUrlsSponsorFile(TestCase):
    """Tests the urls for the dj-sponsoring."""

    def test_sponsor_list_files_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-files-list', kwargs={'pk': 1})
        self.assertEqual(url, "/1/files")

    def test_sponsor_file_create_url(self):
        """Test the URL that adds a file to a specific sponsor."""
        url = reverse('dj_sponsoring:sponsor-file-create', kwargs={'pk': 1})
        self.assertEqual(url, '/1/files/create')

    def test_sponsor_file_detail_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-file-detail', kwargs={'pk': 1})
        self.assertEqual(url, '/files/1')

    def test_sponsor_file_update_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-file-update', kwargs={'pk': 1})
        self.assertEqual(url, "/files/1/update")

    def test_sponsor_file_delete_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-file-delete', kwargs={'pk': 1})
        self.assertEqual(url, "/files/1/delete")
