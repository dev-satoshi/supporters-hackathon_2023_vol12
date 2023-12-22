from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import HomePageView, PostCreateView, PostDeleteView, PostDetailView, PostUpdateView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/create/", PostCreateView.as_view(), name="create-post"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="detail-post"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="update-post"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="delete-post"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
