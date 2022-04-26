from django.urls import reverse
from django.test import TestCase
import datetime

from django.utils import timezone
# Create your tests here.
from blog.models import Post

def create_post():
    return Post(title="Title content",content="Post content", date_posted=datetime.datetime.now())

class HomeViewTests(TestCase):
    def test_post(self):
        response = self.client.get(reverse('blog:post-detail:pk'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Post content")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

