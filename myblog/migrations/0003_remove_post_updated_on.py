# Generated by Django 5.2.1 on 2025-05-29 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_remove_community_description_alter_comment_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_on',
        ),
    ]
