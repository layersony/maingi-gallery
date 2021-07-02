from django.test import TestCase
from .models import Image, Category, Location

class TestImage(TestCase):
  def setUp(self):
    self.location = Location(location='Nairobi')
    self.location.saveLocation()

    self.category = Category(category='Food')
    self.category.saveCategory()

    self.image = Image(image ='photos/test.jpg', image_name = 'test1', image_desc= 'this is a test1', location_id=self.location, category_id=self.category)

  def teardown(self):
    Image.objects.all().delete()
    Location.objects.all().delete()
    Category.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.image, Image))

  def test_saveImage(self):
    self.image.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images)>0)

  def test_updateImage(self):
    self.image.save_image()
    self.image.update_image(self.image.id, 'photos/test2.jpg')
    updated_image = Image.objects.get(id=self.image.id)
    self.assertEqual(updated_image.image, 'photos/test2.jpg')
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
