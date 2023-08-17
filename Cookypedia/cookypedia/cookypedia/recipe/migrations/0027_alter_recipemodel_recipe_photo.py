# Generated by Django 3.2.20 on 2023-08-17 17:15

import cookypedia.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0026_alter_recipemodel_recipe_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='recipe_photo',
            field=models.ImageField(upload_to='photos/', validators=[cookypedia.core.validators.image_size_validator_5mb]),
        ),
    ]
