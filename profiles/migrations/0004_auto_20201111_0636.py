# Generated by Django 3.1.2 on 2020-11-11 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_userprofile_default_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_country',
            new_name='main_country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_county',
            new_name='main_county',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_phone_number',
            new_name='main_phone_number',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_postcode',
            new_name='main_postcode',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_street_address1',
            new_name='main_street_address1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_street_address2',
            new_name='main_street_address2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_town_or_city',
            new_name='main_town_or_city',
        ),
    ]
