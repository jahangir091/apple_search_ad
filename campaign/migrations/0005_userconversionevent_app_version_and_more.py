# Generated by Django 4.2.5 on 2024-02-04 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0004_bulkattributiondata'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconversionevent',
            name='app_version',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userconversionevent',
            name='install_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
