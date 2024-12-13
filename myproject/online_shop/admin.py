from django.contrib import admin
from .models import  Brand, Product, Category, Card, User , Order , OrderProduct, ProductCategory
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Card)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(ProductCategory)
