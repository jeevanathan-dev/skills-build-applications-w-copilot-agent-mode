from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Team, Activity, Leaderboard, Workout

class TeamTests(APITestCase):
    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'Test Team'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        url = reverse('activity-list')
        data = {'user': 'user1', 'team': 'Test Team', 'type': 'run', 'duration': 30}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

class LeaderboardTests(APITestCase):
    def test_create_leaderboard(self):
        url = reverse('leaderboard-list')
        data = {'team': 'Test Team', 'points': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        url = reverse('workout-list')
        data = {'name': 'Push Ups', 'difficulty': 'Easy'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
