import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_home(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200, "Нет доступа к главной странице"