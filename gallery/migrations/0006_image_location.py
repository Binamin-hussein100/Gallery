# Generated by Django 3.2.7 on 2021-09-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_rename_place_category_pic_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ManyToManyField(to='gallery.Location'),
        ),
    ]
