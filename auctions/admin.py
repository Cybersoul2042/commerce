from django.contrib import admin
from .models import Item, Comment, Bid

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    item_list = ["itemUser", "itemName", "itemImage", "itemText", "itemBid", "category", "watchlisted"]

class CommentsAdmin(admin.ModelAdmin):
    comment_list = ["item", "user", "text"]

class BidsAdmin(admin.ModelAdmin):
    bid_list = ["user", "item", "bidAmount"]

admin.site.register(Item, ItemsAdmin)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(Bid, BidsAdmin)
