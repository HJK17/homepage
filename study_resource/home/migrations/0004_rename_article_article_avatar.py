# Generated by Django 3.2.6 on 2021-08-30 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_avatar_article_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article',
            new_name='avatar',
        ),
    ]
