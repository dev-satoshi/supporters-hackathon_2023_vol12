from django.views.generic import TemplateView
from .models import Post
from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import CreatePostForm
from django.views.generic.edit import FormView


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class CreatePostView(TemplateView):
    template_name = "posts/post_create.html"
    form_class = CreatePostForm()
    success_url = '/success/'  # フォーム送信成功後にリダイレクトするURL
