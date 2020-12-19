# Generated by Django 3.1.4 on 2020-12-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20201219_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(error_messages={'blank': "The name field can't be blank.", 'invalid': 'The name field is invalid.', 'max_length': 'The name field must be at most 255 characters.', 'null': "The name field can't be null."}, max_length=255, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(error_messages={'blank': "The code field can't be blank.", 'invalid': 'The code field is invalid.', 'max_length': 'The code field must be at most 255 characters.', 'null': "The code field can't be null."}, max_length=3, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(error_messages={'blank': "The name field can't be blank.", 'invalid': 'The name field is invalid.', 'max_length': 'The name field must be at most 255 characters.', 'null': "The name field can't be null."}, max_length=255, unique=True, verbose_name='Name'),
        ),
    ]
