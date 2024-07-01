from django.contrib import admin
from .models import Item, Comment, Bid, Watchlist

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    item_list = ["itemUser", "itemName", "itemImage", "itemText", "itemBid", "category", "watchlisted"]

class CommentsAdmin(admin.ModelAdmin):
    comment_list = ["item", "user", "comment"]

class BidsAdmin(admin.ModelAdmin):
    bid_list = ["user", "item", "bidAmount"]

class WatchlistsAdmin(admin.ModelAdmin):
    bid_list = ["user", "item"]

admin.site.register(Item, ItemsAdmin)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(Bid, BidsAdmin)
admin.site.register(Watchlist, WatchlistsAdmin)
