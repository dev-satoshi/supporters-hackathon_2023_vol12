from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CreatePostForm, UpdatePostForm
from .models import Post


@method_decorator(cache_page(60 * 15), name="dispatch")
class HomePageView(ListView):
    model = Post
    template_name = "pages/home.html"
    context_object_name = "posts"
    ordering = ["-id"]


class PostCreateView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "pages/post_create.html"
    success_url = reverse_lazy("home")


class PostDetailView(DetailView):
    model = Post
    template_name = "pages/post_detail.html"
    context_object_name = "post"


class PostUpdateView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = "pages/post_update.html"

    def get_success_url(self):
        return reverse("detail-post", kwargs={"pk": self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = "pages/post_delete.html"
    success_url = reverse_lazy("home")

    def delete(self, request, *args, **kwargs):
        return super(PostDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("home")
