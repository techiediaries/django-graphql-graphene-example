# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Product ,Family ,Location ,Transaction  
# Register your models here.

admin.site.register(Product)
admin.site.register(Family)
admin.site.register(Location)
admin.site.register(Transaction)

