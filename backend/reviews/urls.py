from django.urls import path
from . import views

urlpatterns = [
    # /reviews/ +
    # 리뷰
    path('<int:review_pk>/', views.detail_or_update_or_delete_review),
    path('movie/<int:movie_pk>/', views.create_or_list_review),
    path('<int:review_pk>/like/', views.like_review),
    # 댓글
    path('<int:review_pk>/comments/', views.create_comment),
    path('comments/<int:comment_pk>/', views.update_or_delete_comment),
]
