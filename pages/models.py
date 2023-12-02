from django.db import models


class Post(models.Model):
    location_name = models.CharField(max_length=100)
    address = models.TextField()
    post_content = models.TextField()

    def __str__(self):
        return self.location_name
