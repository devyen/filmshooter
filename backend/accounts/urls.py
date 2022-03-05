from django.urls import path
from . import views


urlpatterns = [
    # accounts/ + 
    path('<nickname>/', views.detail_or_create_or_update_profile),
    path('<nickname>/statistic/', views.get_profile_statistic),
    path('<nickname>/reviews/', views.get_reviews),
    path('<nickname>/toprank_reviews/', views.get_toprank_reviews),
    path('<nickname>/like_movies/', views.get_like_movies),
]
