# Generated by Django 3.1 on 2020-08-24 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_auto_20200823_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]