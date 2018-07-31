from django.test import Client
from django.urls import reverse
from django.utils.encoding import force_text

import pytest

pytestmark = pytest.mark.django_db

def test_sponsors_list_view(client):
    r = client.get(reverse('dj_sponsoring:sponsor-list'))
    assert r.status_code == 200
    html = force_text(r.content)
    assert 'No sponsors...' in html