# Generated by Django 3.2.7 on 2021-09-04 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20210904_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='place',
        ),
    ]
