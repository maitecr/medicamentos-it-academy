from django.contrib import admin
from .models import Medicamento

# Register your models here.
#admin.site.register(Medicamento)

@admin.register(Medicamento)
class Medicamento(admin.ModelAdmin):
    list_display = ("produto", "substancia", "ean_1", "comercializado_2020")