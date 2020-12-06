from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView


class HomePageViewTests(SimpleTestCase):

	# this setUp function is the place to define attributes that will be
	# used by muliple other methods so as to keep your code dry
	def setUp(self):
		url = reverse('home')
		self.response = self.client.get(url)

	def test_homepageview_status_code(self):
		self.assertEqual(self.response.status_code, 200)
 
	def test_homepageview_template_used(self):
		self.assertTemplateUsed(self.response, 'pages/home.html')

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


class AboutPageViewTests(SimpleTestCase):
	
	def setUp(self):
		url = reverse('about')
		self.response = self.client.get(url)

	def test_about_page_status_code(self):
		self.assertEqual(self.response.status_code, 200)
	
	def test_about_page_template_used(self):
		self.assertTemplateUsed(self.response, "pages/about.html")

	def test_about_page_contains(self):
		self.assertContains(self.response, "About")

	def test_about_page_does_not_contain(self):
		self.assertNotContains(self.response, "This is your about hahahaha")

	def test_about_page_view_resolves(self):
		view = resolve("/about/")
		self.assertEqual(
			view.func.__name__,
			AboutPageView.as_view().__name__,
		)