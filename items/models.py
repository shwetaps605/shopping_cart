from django.db import models

# Create your models here.

class Item(models.Model):
    item_name=models.CharField(max_length=50)
    quantity=models.IntegerField(default=0)
    price=models.FloatField(default=50.0)
    discount_available=models.IntegerField(default=0)

    def __str__(self):
        return self.item_name