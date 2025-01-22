# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    sku = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    unit = models.CharField(max_length=255, null=True, blank=True)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Warehouse(models.Model):

    #__Warehouse_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    contact_info = models.CharField(max_length=255, null=True, blank=True)

    #__Warehouse_FIELDS__END

    class Meta:
        verbose_name        = _("Warehouse")
        verbose_name_plural = _("Warehouse")


class Batch(models.Model):

    #__Batch_FIELDS__
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    model = models.CharField(max_length=255, null=True, blank=True)
    expire_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    quantity = models.IntegerField(null=True, blank=True)

    #__Batch_FIELDS__END

    class Meta:
        verbose_name        = _("Batch")
        verbose_name_plural = _("Batch")



#__MODELS__END
