from django.urls import path

from .views import HomePageView, AboutPageView, PostCreateView, PostFeedVeiw

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("post_create/", PostCreateView.as_view(), name="post_create"),
    path("post_feed", PostFeedVeiw.as_view() ,name="post_feed")
]
