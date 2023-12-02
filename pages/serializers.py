from rest_framework import serializers
from .models import Post


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post()  # シリアライズするモデル
        fields = ["location_name", "address", "post_content"]  #シリアライズするフィールド
