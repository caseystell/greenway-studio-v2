from django.db import models

class CustomUser(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)
  phone = models.PositiveSmallIntegerField()
  company = models.CharField(max_length=100)
  message = models.TextField()

  def __str__(self):
    return self.email
