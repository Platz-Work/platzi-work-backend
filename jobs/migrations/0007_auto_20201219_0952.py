# Generated by Django 3.1.4 on 2020-12-19 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20201219_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='is_active',
            field=models.BooleanField(default=True, error_messages={'blank': "The is_active field can't be blank.", 'invalid': 'The is_active field is invalid.', 'null': "The is_active field can't be null."}, verbose_name='Active'),
        ),
    ]