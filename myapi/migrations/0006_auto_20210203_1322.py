# Generated by Django 3.1.5 on 2021-02-03 10:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_auto_20210202_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='iin',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length of iin must be 12', regex='^.{12}$')]),
        ),
    ]
