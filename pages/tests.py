from django.test import SimpleTestCase
from django.urls import reverse


class HomePageViewTests(SimpleTestCase):

    def test_homepageview_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepageview_urlname_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
 
    def test_homepageview_template_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

