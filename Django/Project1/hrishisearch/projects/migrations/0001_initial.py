# Generated by Django 4.0.4 on 2022-05-09 07:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('demolink', models.CharField(blank=True, max_length=2000, null=True)),
                ('sourcelink', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
