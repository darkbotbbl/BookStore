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

    def test_homepageview_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, "HomePage")

    def test_homepageview_does_not_contain_correct_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, "I am glad to be a benefactor of this shit!!!")
