# Generated by Django 5.2.3 on 2025-06-26 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='todd', max_length=100)),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(blank=True, max_length=200)),
                ('isbn', models.CharField(blank=True, max_length=20)),
                ('openlibrary_url', models.URLField(blank=True)),
                ('googlebooks_url', models.URLField(blank=True)),
                ('amazon_url', models.URLField(blank=True)),
                ('date_acquired', models.DateField(blank=True, null=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
