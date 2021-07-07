from django.contrib import admin

# Register your models here.
from notes_app import models

admin.site.register(models.Profile)
admin.site.register(models.Note)
