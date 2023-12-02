from django.urls import include, path

from .views import AboutPageView, CreatePostView, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("posts/", CreatePostView.as_view(), name="create-post"),
]
