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
        self.assertEqual(url, '/sponsors/')

    def test_sponsor_create_url(self):
        """Test the URL of that allows the creation of a sponsor."""
        url = reverse('dj_sponsoring:sponsor-create')
        self.assertEqual(url, '/sponsors/create')

    def test_sponsor_detail_url(self):
        """Test the URL that gives the details of a sponsor."""
        url = reverse('dj_sponsoring:sponsor-detail', kwargs={'pk': 1})
        self.assertEqual(url, '/sponsors/1')

    def test_sponsor_update_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-update', kwargs={'pk': 1})
        self.assertEqual(url, "/sponsors/1/update")

    def test_sponsor_delete_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-delete', kwargs={'pk': 1})
        self.assertEqual(url, "/sponsors/1/delete")


class TestUrlsSponsorImage(TestCase):
    """Tests the urls for the dj-sponsoring."""

    def test_sponsor_list_images_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-images-list', kwargs={'pk': 1})
        self.assertEqual(url, "/sponsors/1/images")

    def test_sponsor_image_create_url(self):
        """Test the URL that adds a image to a specific sponsor."""
        url = reverse('dj_sponsoring:sponsor-image-create', kwargs={'pk': 1})
        self.assertEqual(url, '/sponsors/1/images/create')

    def test_sponsor_image_detail_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-image-detail', kwargs={'pk': 1})
        self.assertEqual(url, '/sponsors/images/1')

    def test_sponsor_image_update_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-image-update', kwargs={'pk': 1})
        self.assertEqual(url, "/sponsors/images/1/update")

    def test_sponsor_image_delete_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-image-delete', kwargs={'pk': 1})
        self.assertEqual(url, "/sponsors/images/1/delete")


class TestUrlsSponsorDocument(TestCase):
    """Tests the urls for the dj-sponsoring."""

    def test_sponsor_list_documents_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-documents-list', kwargs={'pk': 1})
        self.assertEqual(url, "/sponsors/1/documents")

    def test_sponsor_document_create_url(self):
        """Test the URL that adds a document to a specific sponsor."""
        url = reverse('dj_sponsoring:sponsor-document-create', kwargs={'pk': 1})
        self.assertEqual(url, '/sponsors/1/documents/create')

    def test_sponsor_document_detail_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-document-detail', kwargs={'pk': 1})
        self.assertEqual(url, '/sponsors/documents/1')

    def test_sponsor_document_update_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-document-update', kwargs={'pk': 1})
        self.assertEqual(url, "/sponsors/documents/1/update")

    def test_sponsor_document_delete_url(self):
        """Test the URL of the listing of sponsors."""
        url = reverse('dj_sponsoring:sponsor-document-delete', kwargs={'pk': 1})
        self.assertEqual(url, "/sponsors/documents/1/delete")
