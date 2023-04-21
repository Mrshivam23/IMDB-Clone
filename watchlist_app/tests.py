from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from watchlist_app.api import serializers
from watchlist_app.models import models


class StreamPlatformTestCase(APITestCase):
    
    
    def setUp(self):
        self.user = User.objects.create_user(username = 'example',
                                            password='password')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token'+self.token.key)
        
        self.stream = models.StreamPlatform.objects.create(name="netflix",about="Best Platform",website="http://www.netflix.com")
        
    def test_streamplatform_create(self):
        data = {
            "name": "netflix",
            "about": "Best Platform",
            "website": "http://www.netflix.com"
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        
    def test_streamplatform_ind(self):
        response = self.client.get(reverse('streamplatform-detail',args=(self.stream.id,))) 
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        
        
    def test_review_user(self):
        response = self.client.get('/watch/reviews/?username' )
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
