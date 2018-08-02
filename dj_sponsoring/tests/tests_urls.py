#!/usr/bin/env python
# coding=utf-8

"""
test_dj-sponsoring
------------

Tests for `dj-sponsoring` urls module.
"""

from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):

    def test_sponsor_list_url(self):
        url = reverse('dj_sponsoring:sponsor-list')
        self.assertEqual(url, '/sponsors')

    def test_sponsor_create_url(self):
        url = reverse('dj_sponsoring:sponsor-create')
        self.assertEqual(url, '/sponsors/create')

    def test_sponsor_detail_url(self):
        url = reverse('dj_sponsoring:sponsor-detail', kwargs={'pk': 1})
        self.assertEqual(url, '/sponsors/1')

    def test_sponsor_update_url(self):
        url = reverse('dj_sponsoring:sponsor-update', kwargs={'pk': 1})
        self.assertEqual(url, "/sponsors/1/update")

    def test_sponsor_delete_url(self):
        url = reverse('dj_sponsoring:sponsor-delete', kwargs={'pk': 1})
        self.assertEqual(url, "/sponsors/1/delete")

    def test_sponsor_image_list_url(self):
        url = reverse('dj_sponsoring:sponsor-image-list')
        self.assertEqual(url, '/sponsors/image')

    def test_sponsor_image_create_url(self):
        url = reverse('dj_sponsoring:sponsor-image-create')
        self.assertEqual(url, '/sponsors/image/create')

    def test_sponsor_image_detail_url(self):
        url = reverse('dj_sponsoring:sponsor-image-detail', kwargs={'pk': 1})
        self.assertEqual(url, '/sponsors/image/1')

    def test_sponsor_image_update_url(self):
        url = reverse('dj_sponsoring:sponsor-image-update', kwargs={'pk': 1})
        self.assertEqual(url, "/sponsors/image/1/update")

    def test_sponsor_image_delete_url(self):
        url = reverse('dj_sponsoring:sponsor-image-delete', kwargs={'pk': 1})
        self.assertEqual(url, "/sponsors/image/1/delete")

    def test_sponsor_document_list_url(self):
        url = reverse('dj_sponsoring:sponsor-document-list')
        self.assertEqual(url, '/sponsors/document')

    def test_sponsor_document_create_url(self):
        url = reverse('dj_sponsoring:sponsor-document-create')
        self.assertEqual(url, '/sponsors/document/create')

    def test_sponsor_document_detail_url(self):
        url = reverse('dj_sponsoring:sponsor-document-detail', kwargs={'pk': 1})
        self.assertEqual(url, '/sponsors/document/1')

    def test_sponsor_document_update_url(self):
        url = reverse('dj_sponsoring:sponsor-document-update', kwargs={'pk': 1})
        self.assertEqual(url, "/sponsors/document/1/update")

    def test_sponsor_document_delete_url(self):
        url = reverse('dj_sponsoring:sponsor-document-delete', kwargs={'pk': 1})
        self.assertEqual(url, "/sponsors/document/1/delete")
