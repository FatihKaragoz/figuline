from django.db import models
import uuid
import time
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class category(models.Model):
    # category_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False, blank=True, unique=True)
    cat_id = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=100, verbose_name="Kategori")
    categoryExp = models.CharField(max_length=100, verbose_name="Aciklama")
    catImage = models.ImageField(verbose_name="Kateori Menü Resmi")

    def __str__(self):
        return str(self.cat_id)

class products(models.Model):
    # product_id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False,blank=True,unique=True)
    pro_id = models.AutoField(primary_key=True)
    productCaption = models.CharField(max_length=100,verbose_name="Başlık")
    cat = models.ForeignKey(category,verbose_name="Cat",related_name="category2category",on_delete=models.CASCADE)
    productContain = models.CharField(max_length=1000,verbose_name="Ürün açıklaması")
    image1 = models.ImageField(verbose_name="Urun Resmi 1")
    image2 = models.ImageField(verbose_name="Urun Resmi 2")
    image3 = models.ImageField(verbose_name="Urun Resmi 3")
    image4 = models.ImageField(verbose_name="Urun Resmi 4")

    def __str__(self):
        # return str(self.pro_id)
        return self.productCaption


class newArrivals(models.Model):
    # newArrivals_id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False,blank=True,unique=True)
    newAr_id = models.AutoField(primary_key=True)
    urun = models.ForeignKey(products, verbose_name="Ürün", related_name="urun1urun",on_delete=models.CASCADE)

    def __str__(self):
        return str(self.newAr_id)


class about(models.Model):
    about_id = models.AutoField(primary_key=True)
    image = models.ImageField(verbose_name="Hakkımızda image")
    text1 = models.CharField(max_length=1000,verbose_name="Hakkımızda yazı 1 ")
    text2 = models.CharField(max_length=1000,verbose_name="Hakkımızda yazı 2 ")
    text3 = models.CharField(max_length=1000,verbose_name="Hakkımızda yazı 3 ")


    def __str__(self):
        return self.text1


class contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    image = models.ImageField(verbose_name="İletişim image")
    text1 = models.CharField(max_length=1000,verbose_name="İletişim yazı 1")
    address = models.CharField(max_length=1000,verbose_name="Adresimiz")
    phone = models.CharField(max_length=25,verbose_name="Telefon numaramız")
    email = models.CharField(max_length=40,verbose_name="E-mail adresimiz")
    coordinatelat = models.CharField(max_length=40,verbose_name="Koordinatlarımız - Lat ")
    coordinatelong = models.CharField(max_length=40,verbose_name="Koordinatlarımız - Long")


    def __str__(self):
        return self.text1

