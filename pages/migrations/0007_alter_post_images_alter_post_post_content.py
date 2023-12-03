# Generated by Django 4.2.5 on 2023-12-03 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_post_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(max_length=255, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=models.TextField(blank=True),
        ),
    ]
