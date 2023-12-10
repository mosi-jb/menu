from django.contrib import admin

from .models import Category, Product


# Register your models here.

class ProductInline(admin.StackedInline):
    model = Product
    extra = 2


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ProductInline]


admin.site.register(Product)
