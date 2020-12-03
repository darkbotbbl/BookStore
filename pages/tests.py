from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView


class HomePageViewTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepageview_status_code(self):
        self.assertEqual(self.response.status_code, 200)
 
    def test_homepageview_template_used(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepageview_contains_correct_html(self):
        self.assertContains(self.response, "HomePage")

    def test_homepageview_does_not_contain_correct_html(self):
        self.assertNotContains(self.response, "I am glad to be a benefactor of this shit!!!")

    def test_homepage_url_resolves_to_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )