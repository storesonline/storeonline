# Generated by Django 3.1.8 on 2021-04-20 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210420_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat_items',
            name='image',
            field=models.ImageField(default='static/home/images/dummy.jpg', upload_to='static/home/images'),
        ),
        migrations.AlterField(
            model_name='cat_items',
            name='image3',
            field=models.ImageField(blank=True, default='static/home/images/dummy.jpg', null=True, upload_to='static/home/images'),
        ),
    ]
