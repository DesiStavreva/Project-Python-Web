# Generated by Django 3.2.20 on 2023-08-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0002_alter_cocktailmodel_cocktail_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktailmodel',
            name='cocktail_photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
