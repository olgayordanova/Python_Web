from django.contrib import admin

# Register your models here.
from tracker import models

admin.site.register(models.Profile)
admin.site.register(models.Expense)