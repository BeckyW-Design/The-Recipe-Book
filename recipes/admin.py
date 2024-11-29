from django.contrib import admin
from .models import RecipeCard, Ingredient, Comment
from django_summernote.admin import SummernoteModelAdmin




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

class CommentAdmin(SummernoteModelAdmin):
    list_display = ['author', 'body']
    list_filter = ['author'] 
    search_fields = ['author']

class IngredientAdmin(SummernoteModelAdmin):
    list_display = ['name', 'unit']
    list_filter = ['name'] 
    search_fields = ['name']   

admin.site.register(RecipeCard, RecipeCardAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Ingredient, IngredientAdmin)