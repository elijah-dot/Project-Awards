# Generated by Django 4.0.5 on 2022-06-12 23:15

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('project_name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=2000)),
                ('category', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('url', models.URLField(max_length=60, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('average_score', models.FloatField(default=0)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_rate', models.IntegerField(blank=True, default=0, null=True)),
                ('usability_rate', models.IntegerField(blank=True, default=0, null=True)),
                ('content_rate', models.IntegerField(blank=True, default=0, null=True)),
                ('average', models.IntegerField(blank=True, default=0, null=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='present.project')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_photo', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('bio', models.TextField(blank=True, max_length=1000, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
