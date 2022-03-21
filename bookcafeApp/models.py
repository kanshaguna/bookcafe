from django.db import models

# Create your models here.
class Menu(models.Model):
    itemName = models.CharField(max_length=30)
    itemCategory = models.CharField(max_length=30)
    itemPrice = models.FloatField()


class Enquiry(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    contact = models.IntegerField()
    message = models.TextField(max_length=300)






