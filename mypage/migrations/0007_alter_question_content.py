# Generated by Django 4.2.2 on 2023-06-28 08:42

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0006_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
