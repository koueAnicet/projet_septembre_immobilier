# Generated by Django 4.1.1 on 2022-09-29 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0003_alter_submitproperty_name_alter_submitproperty_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitproperty',
            name='user_property_submit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submit_user', to=settings.AUTH_USER_MODEL),
        ),
    ]