# Generated by Django 3.1.2 on 2020-10-13 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20201011_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 15, 17, 50, 24, 946068)),
        ),
    ]