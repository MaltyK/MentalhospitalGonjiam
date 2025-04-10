import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_registr_user(client):
    url = reverse('registr')
    data = {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password1': 'VeryStrongPass123',
        'password2': 'VeryStrongPass123'
    }
    response = client.post(url, data)
    assert response.status_code == 302, "После регистрации не произошло перенаправление"
    assert User.objects.filter(username='newuser').exists(), "Пользователь не создан"