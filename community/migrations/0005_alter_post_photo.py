# Generated by Django 4.2.2 on 2023-06-23 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='community/images/%Y/%m/%d/'),
        ),
    ]
