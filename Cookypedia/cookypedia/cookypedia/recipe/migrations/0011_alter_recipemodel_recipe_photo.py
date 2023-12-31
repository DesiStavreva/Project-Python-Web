# Generated by Django 3.2.20 on 2023-08-10 16:45

import cookypedia.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0010_alter_recipemodel_recipe_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='recipe_photo',
            field=models.ImageField(null=True, upload_to='', validators=[cookypedia.core.validators.image_size_validator_5mb]),
        ),
    ]
