# Generated by Django 3.2 on 2021-05-11 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_radiostation', '0022_remove_base_rs_lifetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='base_rs',
            name='lifetime_int',
            field=models.CharField(default='lifetime', max_length=250, verbose_name='Срок эксплуатации'),
        ),
    ]