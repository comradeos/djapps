# Generated by Django 4.0.6 on 2022-10-03 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tomato', '0003_salesorder_text_alter_salesorder_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 3, 20, 37, 58, 569261)),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='text',
            field=models.TextField(default='lol'),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 10, 3, 20, 37, 58, 569343)),
        ),
    ]