# Generated by Django 3.2.20 on 2023-08-13 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='to_photo',
            new_name='to_recipe',
        ),
    ]