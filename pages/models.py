from django.db import models


# Create your models here.
class Post(models.Model):
    location_name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    post_content = models.CharField(max_length=500)

    def __str__(self):
        return self.post_content
