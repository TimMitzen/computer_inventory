from django.conf import urls
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from computer_inventory.views import display_computers, add_computer, index, SearchResults
# Create your tests here.
class ComputerTestCase(SimpleTestCase):
   def test_display_url(self):
      url = reverse('display_computers')
      self.assertEquals(resolve(url).func, display_computers)#makes sure url matchs the display computer

   def test_add_url(self):
      url = reverse('add_computer')
      self.assertEquals(resolve(url).func, add_computer)

   def test_index_url(self):
      url = reverse('index')
  
      self.assertEquals(resolve(url).func, index)
   
   def test_search_url(self):
      path = reverse('Search Results')
      self.assertEquals(resolve(path).func.view_class, SearchResults)