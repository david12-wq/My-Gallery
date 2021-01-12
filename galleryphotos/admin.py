from django.contrib import admin
from .models import Image, Location, Category

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal=('category','location')

    admin.site.register(Category)
    admin.site.register(Location)
    admin.site.register(Image)
