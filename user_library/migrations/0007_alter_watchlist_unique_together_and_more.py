# Generated by Django 5.1.4 on 2025-02-03 09:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_library', '0006_alter_likedserie_unique_together_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='watchlist',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='content_type',
            field=models.CharField(blank=True, choices=[('movie', 'Movie'), ('serie', 'Serie')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='WatchedContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('movie', 'Movie'), ('serie', 'Serie')], max_length=25)),
                ('object_id', models.PositiveIntegerField()),
                ('rating', models.IntegerField(blank=True, choices=[(1, '1 - Terrible'), (2, '2 - Very Bad'), (3, '3 - Bad'), (4, '4 - Poor'), (5, '5 - Average'), (6, '6 - Fair'), (7, '7 - Good'), (8, '8 - Very Good'), (9, '9 - Excellent'), (10, '10 - Masterpiece')], null=True)),
                ('rewatch', models.CharField(blank=True, choices=[('never', 'Never again.'), ('no', 'Once was enough.'), ('maybe', 'Maybe in some years.'), ('worth', "It's Worth a rewatch."), ('totally', 'Must rewatch it!')], null=True)),
                ('watched_at', models.DateTimeField(auto_now_add=True)),
                ('personal_note', models.TextField(blank=True, max_length=2000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watched_movies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'watched_content',
                'verbose_name_plural': 'watched_contents',
                'db_table': 'watched_content',
            },
        ),
        migrations.DeleteModel(
            name='WatchedMovie',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='movie',
        ),
    ]
