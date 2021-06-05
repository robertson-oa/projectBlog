# Generated by Django 3.2 on 2021-05-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('entry_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('category', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=255)),
                ('publication_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
                ('category_description', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('tag_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
    ]