from . import views
from django.urls import path, include

urlpatterns = [
    path('', 
        views.HomePage.as_view(), name='home'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]
