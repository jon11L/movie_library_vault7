# Generated by Django 5.1.4 on 2025-02-03 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_library', '0008_alter_like_options_alter_watchedcontent_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ['-liked_on'], 'verbose_name': 'like', 'verbose_name_plural': 'likes'},
        ),
        migrations.AlterModelTable(
            name='like',
            table='like',
        ),
    ]
