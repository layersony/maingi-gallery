from django.db import models


class Image(models.Model):
  image = models.ImageField(upload_to='photos')
  image_name =  models.CharField(max_length=200)
  image_desc = models.TextField()
  location_id = models.ForeignKey
  date_upload = models.DateTimeField(auto_now_add=True)

  def save_image(self):
    pass

  def delete_image(self):
    pass

  def update_image(self):
    pass

  @classmethod
  def get_image_by_is(cls, id):
    pass

  @classmethod
  def search_image(cls, category):
    pass

  @classmethod
  def filter_by_location(location):
    pass

  def __str__(self):
    return self.image_name

class Location(models.Model):
  location = models.CharField(max_length=200)

  def __str__(self):
    return self.location

class Category(models.Model):
  category = models.CharField(max_length=200)

  def __str__(self):
    return self.category