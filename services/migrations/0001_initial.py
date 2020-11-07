# Generated by Django 3.1.2 on 2020-11-07 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('image_url', models.URLField(max_length=1024, null=True)),
                ('quizz', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
