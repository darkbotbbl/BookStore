from django.test import SimpleTestCase
from django.urls import reverse


class HomePageViewTests(SimpleTestCase):

    # test the response code of the homepage route
    def test_homepageview_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # test the response code of the reverse of the homepage route
    def test_homepageview_urlname_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
