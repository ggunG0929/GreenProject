# Generated by Django 4.2.2 on 2023-06-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='url',
            field=models.URLField(default='', verbose_name='Site URL'),
        ),
    ]
