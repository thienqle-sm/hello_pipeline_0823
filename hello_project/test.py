from django.http import response
from django.test import SimpleTestCase

class HomePageTests(SimpleTestCase):

    def test_admin_page_status_code(self):
        print("Verify admin page")
        response = self.client.get('/admin')
        self.assertEquals(response.status_code,301)
        # admin -> login

    def test_about_page_status_code(self):
        print("Verify not exist about page")
        response = self.client.get('/about')
        self.assertEquals(response.status_code,404)
          # about 404