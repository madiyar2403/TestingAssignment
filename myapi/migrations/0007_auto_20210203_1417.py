# Generated by Django 3.1.5 on 2021-02-03 11:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_auto_20210203_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='iin',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length of iin must be 12', regex='^[0-9]{12}$')]),
        ),
    ]