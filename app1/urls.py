
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('marks/',views.Marks,name='marks'),
    path('leaderboard/',views.leaderboard,name='leaderboard'),
    path('search/',views.search,name='search'),
    
]