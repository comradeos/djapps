# Generated by Django 4.0.6 on 2022-10-04 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tomato', '0005_alter_salesorder_date_alter_salesorder_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesorder',
            name='bool',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='date',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='email',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='float',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='text',
        ),
        migrations.RemoveField(
            model_name='salesorder',
            name='time',
        ),
    ]
