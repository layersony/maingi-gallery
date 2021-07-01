from django.db import models


class Image(models.Model):
  image = models.ImageField(upload_to='photos')
  image_name =  models.CharField(max_length=200)
  image_desc = models.TextField()
  location_id = models.ForeignKey
  date_upload = models.DateTimeField(auto_now_add=True)


