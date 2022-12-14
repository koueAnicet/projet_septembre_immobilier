# Generated by Django 4.1.1 on 2022-10-13 23:55

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0019_rename_name_city_city_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailvisitor',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='emailvisitor',
            name='phonevisitor',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region='CI'),
        ),
    ]
