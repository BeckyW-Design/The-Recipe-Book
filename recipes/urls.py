from . import views
from django.urls import path, include

urlpatterns = [
    path('', 
        views.RecipeList.as_view(), name='home'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('<slug:slug>/', views.recipe_book, name='recipe_book'),
    path("<int:event_id>/", views.event_detail, name="event_detail"),
]
