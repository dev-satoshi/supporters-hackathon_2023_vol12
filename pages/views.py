from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import CreatePostForm
from .models import Post


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class CreatePostView(FormView):
    template_name = "posts/post_create.html"
    form_class = CreatePostForm
    success_url = "/success/"  # フォーム送信成功後にリダイレクトするURL

    def form_valid(self, form):
        #  フォームのデータ保存などの処理
        form.save()
        print("ok")
        # form.cleaned_dataを使用してフォームのデータにアクセス
        return super().form_valid(form)

    def form_invalid(self, form):
        #  フォームのデータが無効な場合の処理
        print(form.errors)
        return super().form_invalid(form)
