# Generated by Django 4.2.5 on 2023-09-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_record_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
