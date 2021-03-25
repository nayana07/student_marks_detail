
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('sci/',views.sci,name='sci'),
    path('sci_marks/',views.scicence_marks,name='sci_marks'),
    path('sci_leaderboard/',views.science_leaderboard,name='sci_leaderboard'),
    path('sci_search/',views.sci_search,name='sci_search'),
    path('art/',views.art,name='art'),
    path('arts_marks/',views.arts_marks,name='arts_marks'),
    path('art_leaderboard/',views.art_leaderboard,name='art_leaderboard'),
    path('art_search/',views.art_search,name='art_search'),
    path('commerce/',views.commerce,name='commerce'),
    path('com_marks/',views.com_marks,name='com_marks'),
    path('commerce_leaderboard/',views.commerce_leaderboard,name='commerce_leaderboard'),
    path('commerce_search/',views.commerce_search,name='commerce_search'),
]