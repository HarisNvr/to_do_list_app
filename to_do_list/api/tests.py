from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from tasks.models import ToDo


class ToDoTests(APITestCase):
    username = 'test_user',
    password = 'test_pass_123'

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )
        self.client.login(
            username=self.username,
            password=self.password
        )
        self.todo = ToDo.objects.create(
            title='Some_Task',
            description='Some_Description',
            user=self.user
        )

    def test_create_task(self):
        data = {'title': 'New Task'}
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_task(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        data = {'title': 'Updated Task', 'description': 'Updated Description'}
        response = self.client.put(f'/api/tasks/{self.todo.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(f'/api/tasks/{self.todo.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
