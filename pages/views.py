from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class PostCreateView(TemplateView):
    template_name = "posts/post_create.html"

class PostFeedVeiw(TemplateView):
    template_name = "posts/post_feed.html"
