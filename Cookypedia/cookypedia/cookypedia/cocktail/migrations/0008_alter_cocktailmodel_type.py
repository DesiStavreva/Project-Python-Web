# Generated by Django 3.2.20 on 2023-08-17 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0007_alter_cocktailmodel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktailmodel',
            name='type',
            field=models.CharField(choices=[('-------', 'MAKE_YOUR_CHOICE'), ('Alcoholic', 'ALCOHOLIC'), ('Non-Alcoholic', 'NON_ALCOHOLIC')], max_length=13),
        ),
    ]
