from django.contrib import admin
from .models import Enseignant, Cours

# Register your models here.

admin.site.register(Enseignant)
admin.site.register(Cours)
