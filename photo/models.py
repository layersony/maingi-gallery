from django.db import models

class Location(models.Model):
  location = models.CharField(max_length=200)

  def saveLocation(self):
    self.save()

  def __str__(self):
    return self.location

class Category(models.Model):
  category = models.CharField(max_length=200)

  def saveCategory(self):
    self.save()

  def __str__(self):
    return self.category

class Image(models.Model):
  image = models.ImageField(upload_to='photos')
  image_name =  models.CharField(max_length=200)
  image_desc = models.TextField()
  location_id = models.ForeignKey(Location, on_delete=models.CASCADE, default=None)
  category_id = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
  date_upload = models.DateTimeField(auto_now_add=True)

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

  @classmethod
  def update_image(cls, id, imagechange):
    cls.objects.filter(id = id).update(image = imagechange)

  @classmethod
  def get_images_by_id(cls, id):
    try:
      image = cls.objects.get(id=id)
      return image
    except Image.DoesNotExist:
      print('Image does not exist')

  @classmethod
  def search_image(cls, category):
    pass

  @classmethod
  def filter_by_location(location):
    pass

  def __str__(self):
    return self.image_name