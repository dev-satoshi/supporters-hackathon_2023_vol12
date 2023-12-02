from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Post
from .serializers import PostModelSerializer


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class PostCreateView(TemplateView):
    template_name = "posts/post_create.html"


class PostFeedView(TemplateView):
    template_name = "posts/post_feed.html"


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
