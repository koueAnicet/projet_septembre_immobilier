# Generated by Django 4.1.1 on 2022-09-30 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_country_created_alter_infopiece_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description_agent_estate',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]