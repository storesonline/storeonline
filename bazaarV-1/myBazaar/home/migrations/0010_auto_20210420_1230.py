# Generated by Django 3.1.8 on 2021-04-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210420_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat_items',
            name='image2',
            field=models.ImageField(blank=True, default='static/home/images/dummy.jpg', null=True, upload_to='static/home/images'),
        ),
    ]
