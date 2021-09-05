# Generated by Django 3.2.7 on 2021-09-05 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20210905_1207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-pk'], 'verbose_name_plural': 'Images'},
        ),
        migrations.RemoveField(
            model_name='image',
            name='location',
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='gallery.location'),
        ),
    ]
