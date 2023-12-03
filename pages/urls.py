from django.urls import path

from .views import (
    AboutPageView,
    HomePageView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("post/", PostCreateView.as_view(), name="create-post"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="detail-post"),
    path("post/<int:pk>/", PostDeleteView.as_view(), name="delete-post"),
]
