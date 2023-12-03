from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    location_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    post_content = models.TextField()
    images = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_content
