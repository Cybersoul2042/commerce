from django.contrib import admin
from .models import Item

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    item_list = ["itemUser", "itemName", "itemImage", "itemText", "itemStartBid"]

admin.site.register(Item, ItemsAdmin)
