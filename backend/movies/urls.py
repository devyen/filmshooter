from django.urls import path
from . import views

urlpatterns = [
    # /movies/ +
    path('fetch_genres', views.fetch_genres),
    path('fetch_movies', views.fetch_movies),

    path('', views.get_movie_list),
    path('<int:movie_pk>/', views.get_movie_detail),
    path('<int:movie_pk>/like/', views.like_movie),
    path('recommended/', views.recommend),
]
