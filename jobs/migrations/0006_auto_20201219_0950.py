# Generated by Django 3.1.4 on 2020-12-19 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20201219_0925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Currencies'},
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Technologies'},
        ),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(error_messages={'blank': "The code field can't be blank.", 'invalid': 'The code field is invalid.', 'max_length': 'The code field must be at most 255 characters.', 'null': "The code field can't be null."}, max_length=3, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='benefits',
            field=models.TextField(blank=True, error_messages={'blank': "The benefits field can't be blank.", 'invalid': 'The benefits field is invalid.', 'null': "The benefits field can't be null."}, null=True, verbose_name='Benefits'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='cities',
            field=models.CharField(blank=True, error_messages={'blank': "The cities field can't be blank.", 'invalid': 'The cities field is invalid.', 'max_length': 'The cities field must be at most 255 characters.', 'null': "The cities field can't be null."}, max_length=100, null=True, verbose_name='cities'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='country',
            field=models.ForeignKey(blank=True, error_messages={'blank': "The country_id field can't be blank.", 'invalid': 'The country_id field is invalid.', 'null': "The country_id field can't be null."}, null=True, on_delete=django.db.models.deletion.PROTECT, to='jobs.country'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='soft_skills',
            field=models.TextField(blank=True, error_messages={'blank': "The soft_skills field can't be blank.", 'invalid': 'The soft_skills field is invalid.', 'null': "The soft_skills field can't be null."}, null=True, verbose_name='Soft skills'),
        ),
    ]
