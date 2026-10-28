from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    def setUp(self):
        self.email = "test@user.ru"
        self.password = "1234"

    def test_user_registration(self):
        data = {
            "email": self.email,
            "password": self.password,
        }
        response = self.client.post("/users/register", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="test@user.ru").exists())
