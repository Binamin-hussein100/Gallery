# Generated by Django 3.2.7 on 2021-09-04 16:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_image_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
        ),
    ]
