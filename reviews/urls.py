from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('thank-you', views.thankYouView.as_view()),
    path('review-list', views.reviewsListView.as_view()),
    path('reviews/favorite', views.AddFavoriteView.as_view()),
    path('reviews/<int:pk>', views.reviewDetail.as_view()),
    path('image-downloader', views.insertLinkView.as_view())
]
    