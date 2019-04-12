from django.db import models

# Create your models here.

class Img(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
