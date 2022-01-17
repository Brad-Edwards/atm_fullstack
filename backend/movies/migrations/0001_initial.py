# Generated by Django 4.0.1 on 2022-01-17 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('release_year', models.DateField()),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('poster_uri', models.CharField(blank=True, max_length=255, null=True)),
                ('last_admin_update', models.DateField(blank=True, null=True)),
                ('last_data_store_update', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieDataStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('api_key', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.BooleanField()),
                ('date', models.DateField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]