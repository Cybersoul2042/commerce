from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Item(models.Model):
    itemUser = models.ForeignKey(User, related_name = "Item_Owner", on_delete = models.CASCADE)
    itemName = models.CharField(max_length=64)
    itemImage = models.URLField()
    itemText = models.TextField()
    itemStartBid = models.FloatField()

    def __str__(self):
        return self.itemName
