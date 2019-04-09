from django.contrib import admin
from .models import Product, Offer

#List all the fields to display
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

#Commit all the changes
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
