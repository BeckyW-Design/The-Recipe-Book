from django.contrib import admin
from .models import Ingredient
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class IngredientAdmin(SummernoteModelAdmin):
    list_display = ['recipe', 'name', 'quantity', 'unit']
    list_filter = ['name'] 
    search_fields = ['name']  

admin.site.register(Ingredient, IngredientAdmin)

