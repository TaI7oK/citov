# Generated by Django 3.2 on 2021-05-06 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_radiostation', '0011_alter_base_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Base',
            new_name='Base_rs',
        ),
    ]