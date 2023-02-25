from django.db import models
from django.contrib.auth.models import User

#from __future__ import unicode_literals
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin)
from django.forms import ModelForm

class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='')
   image=models.CharField(max_length=200,default="test/1.jpg") 

   def __str__(self):
      return self.name


class Menu(models.Model):
    title = models.CharField(_("title"), max_length=255)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    inventory = models.IntegerField(_("inventory"))

    class Meta:
        verbose_name = _("menu")
        verbose_name_plural = _("menus")

    def __str__(self):
        return f"{self.title} : {str(self.price)}"


class Booking(models.Model):
    name = models.CharField(_("name"), max_length=255)
    guests_number = models.IntegerField(_("guests_number"))
    booking_date = models.DateTimeField(_("booking date"))

    class Meta:
        verbose_name = _("booking")
        verbose_name_plural = _("bookings")

    def __str__(self):
        return self.
