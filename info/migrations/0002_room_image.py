# Generated by Django 4.2 on 2023-04-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, upload_to='img/'),
        ),
    ]