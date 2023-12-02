from django.db import models


# Create your models here.
class Post(models.Model):
    location_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    OPTION_ONE = '1'
    OPTION_TWO = '2'
    OPTION_THREE = '3'
    CATEGORY = [
        (OPTION_ONE, 'カフェ'),
        (OPTION_TWO, 'レストラン'),
        (OPTION_THREE, '公園')
    ]
    category = models.CharField(max_length=2, choices=CATEGORY, default=OPTION_ONE)
    post_content = models.TextField()

    def __str__(self):
        return self.post_content
