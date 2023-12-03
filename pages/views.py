from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView

from .forms import CreatePostForm
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "pages/home.html"
    context_object_name = "posts"


class PostCreateView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "pages/post_create.html"
    success_url = reverse_lazy("home")


class PostDetailView(DetailView):
    model = Post
    template_name = "pages/post_detail.html"
    context_object_name = "post"

class PostDeleteView(DeleteView):
    model = Post
    template_name = "pages/post_delete.html"
    success_url = "/"
