# Generated by Django 5.1 on 2024-08-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('job', models.CharField(max_length=50)),
                ('avatar', models.ImageField(upload_to='users/avatars/')),
                ('avatar_thumbnail', models.ImageField(upload_to='users/thumbnails/')),
            ],
        ),
    ]
