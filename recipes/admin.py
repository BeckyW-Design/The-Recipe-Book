from django.contrib import admin
from .models import RecipeCard
from django_summernote.admin import SummernoteModelAdmin


# @admin.register(RecipeCard)

class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'timings', 'status','category','tag')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'tag': ('title',)}
    summernote_fields = ('description',)

class RecipeCardAdmin(SummernoteModelAdmin):
    list_display = ['title', 'servings', 'timings', 'category', 'status']
    list_filter = ['category', 'status'] 
    search_fields = ['title', 'description']  

admin.site.register(RecipeCard, RecipeCardAdmin)