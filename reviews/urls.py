from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('thank-you', views.thankYouView.as_view()),
    path('review-list', views.reviewsListView.as_view())
]
    