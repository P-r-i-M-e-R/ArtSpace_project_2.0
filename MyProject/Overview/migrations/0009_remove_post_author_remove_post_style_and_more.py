# Generated by Django 5.1 on 2024-08-26 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Overview', '0008_alter_post_author_alter_post_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='style',
        ),
        migrations.RemoveField(
            model_name='post',
            name='type',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Style',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
