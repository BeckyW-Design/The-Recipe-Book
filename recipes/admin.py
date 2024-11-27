from django.contrib import admin
from .models import RecipeCard
from django_summernote.admin import SummernoteModelAdmin


@admin.register(RecipeCard)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'timings', 'status','category','tag')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'tag': ('title',)}
    summernote_fields = ('description',)

# Register your models here.

# admin.register(RecipeCard)
