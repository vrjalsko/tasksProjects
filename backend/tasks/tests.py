from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Users, Task, Project
from .serializers import UsersSerializer, TaskSerializer, ProjectSerializer

class UsersTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'nom': 'John', 'prenom': 'Doe', 'username': 'johndoe', 'email': 'john@gmail.com', 'password': 'john300'}
        self.response = self.client.post(reverse('user-list'), self.user_data, format='json')

    def test_create_user(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_user(self):
        user = Users.objects.get()
        response = self.client.get(reverse('user-detail', kwargs={'pk': user.pk}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nom'], self.user_data['nom'])

    def test_update_user(self):
        user = Users.objects.get()
        updated_data = {'nom': 'Updated Name'}
        response = self.client.put(reverse('user-detail', kwargs={'pk': user.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nom'], updated_data['nom'])

    def test_delete_user(self):
        user = Users.objects.get()
        response = self.client.delete(reverse('user-detail', kwargs={'pk': user.pk}), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)




