# Generated by Django 4.1.1 on 2022-10-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_remove_submitproperty_price_range_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitproperty',
            name='desc_parking',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
    ]