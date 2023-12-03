from django.forms import ModelForm
from .models import Post


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['location_name', 'address', 'category', 'images', 'post_content']
