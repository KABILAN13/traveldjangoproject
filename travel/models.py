from django.db import models

# Create your models here.
class destination(models.Model):

    name = models.CharField(max_length= 30)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(max_length=500)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
