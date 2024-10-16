# Generated by Django 5.1.1 on 2024-09-28 02:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_characteristicskey_characteristicsvalue_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcharacteristics',
            options={'verbose_name_plural': 'ProductCharacteristics'},
        ),
        migrations.AlterField(
            model_name='productcharacteristics',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characteristics', to='products.product'),
        ),
    ]
