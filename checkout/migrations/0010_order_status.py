# Generated by Django 3.1.2 on 2020-11-20 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_auto_20201120_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='not_paid', max_length=50),
        ),
    ]
