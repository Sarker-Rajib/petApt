# Generated by Django 4.2.7 on 2024-01-26 13:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pets/media/images/')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('adapt_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('body', models.TextField(verbose_name='Your Feedback')),
                ('created_on', models.DateTimeField(default=datetime.datetime(2024, 1, 26, 19, 59, 56, 376606))),
                ('Pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='Pets.pet')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pets.petcategory'),
        ),
    ]
