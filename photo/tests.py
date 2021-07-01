from django.test import TestCase
from .models import Image, Category, Location

class TestImage(TestCase):
  def setUp(self):
    self.image = Image(image ='photos/test,jpg', image_name = 'test1', image_desc= 'this is a test1')

  def test_instance(self):
    self.assertTrue(isinstance(self.image, Image))

  def test_saveImage(self):
    self.image.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images)>0)

class TestLocation(TestCase):
  def setUp(self):
    self.location = Location(location='Nairobi')

  def test_instance(self):
    self.assertTrue(isinstance(self.location, Location))


  def test_saveLocation(self):
    self.location.saveLocation()
    location = Location.objects.all()
    self.assertTrue(len(location)>0)

class TestCategory(TestCase):
  def setUp(self):
    self.category = Category(category='Food')

  def test_instance(self):
    self.assertTrue(isinstance(self.category, Category))

  def test_saveCategory(self):
    self.category.saveCategory()
    category = Category.objects.all()
    self.assertTrue(len(category)>0)
