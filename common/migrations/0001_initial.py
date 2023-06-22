# Generated by Django 4.2.2 on 2023-06-22 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=150)),
                ('address', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('regdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
