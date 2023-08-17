# Generated by Django 3.2.20 on 2023-08-17 16:38

import cookypedia.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0025_alter_recipemodel_recipe_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='recipe_photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/', validators=[cookypedia.core.validators.image_size_validator_5mb]),
        ),
    ]
