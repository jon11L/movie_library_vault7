# Generated by Django 5.1.4 on 2025-02-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_rename_trailer_youtube_id_movie_trailers'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='spoken_languages',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
