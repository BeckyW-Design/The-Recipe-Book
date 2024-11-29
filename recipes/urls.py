from . import views
from django.urls import path, include

urlpatterns = [
    path('', 
        views.HomePage, name='home'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('<slug:slug>/', views.recipe_book, name='recipe_book'),
]
