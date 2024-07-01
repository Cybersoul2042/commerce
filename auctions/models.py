from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Item(models.Model):
    itemUser = models.ForeignKey(User, related_name = "Item_Owner", on_delete = models.CASCADE)
    itemName = models.CharField(max_length=64)
    itemImage = models.TextField()
    itemText = models.TextField()
    itemBid = models.FloatField()
    category = models.TextField()
    watchlisted = models.BooleanField(default = False)
    code = models.CharField(max_length=12)

    def serialize(self):
        return {
            "itemName": self.itemName,
            "itemImage": self.itemImage
        }
    
class Bid(models.Model):
    user = models.ForeignKey(User, related_name = "Bid_User", on_delete = models.CASCADE)
    item = models.ForeignKey(Item, related_name = "Bid_Item", on_delete = models.CASCADE)
    bidAmount = models.FloatField()

    def serialized(self):
        return {
            "BidUser": self.user,
            "BidItem": self.itemName,
            "BidAmount": self.bidAmount
        }
    
class Comment(models.Model):
    item = models.ForeignKey(Item, related_name = "Comment_Item", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name = "Comment_User", on_delete = models.CASCADE)
    comment = models.CharField(max_length = 256)

    def serialize(self):
        return {
            "comment": self.comment
        }
    
class Watchlist(models.Model):
    user = models.ForeignKey(User, related_name="User_Watchlist", on_delete = models.CASCADE)
    item = models.ForeignKey(Item, related_name="Item_Watchlist", on_delete = models.CASCADE)

    def serialize(self):
        return {
            "item": self.item
        }