# Generated by Django 4.1.1 on 2022-10-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0015_alter_areaproperty_active_alter_bathnumber_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVisitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailvisitor', models.EmailField(max_length=254)),
            ],
        ),
    ]
