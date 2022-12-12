from django.contrib import admin
from .models import *

'''
user: admin
pass: Baylor ID
'''
# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)