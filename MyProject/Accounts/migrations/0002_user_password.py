# Generated by Django 5.1 on 2024-08-26 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=0, max_length=128),
            preserve_default=False,
        ),
    ]
