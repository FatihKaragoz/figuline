from django.contrib import admin
from model import models
from .models import products,newArrivals,category,about,contact

class categoryAdmin(admin.ModelAdmin):
    list_display = ("categoryName","categoryExp","cat_id")
admin.site.register(category,categoryAdmin)

class productAdmin(admin.ModelAdmin):
    list_display = ("productCaption","productContain")
admin.site.register(products,productAdmin)

class newArrivalAdmin(admin.ModelAdmin):
    list_display = ("newAr_id",)
admin.site.register(newArrivals,newArrivalAdmin)
# Register your models here.


class contactAdmin(admin.ModelAdmin):
    list_display = ("text1","address","phone","email","coordinatelat","coordinatelong")

admin.site.register(contact,contactAdmin)

class aboutAdmin(admin.ModelAdmin):
    list_display = ("text1","text2","text3")

admin.site.register(about,aboutAdmin)