# Generated by Django 4.2 on 2023-05-02 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_reporting_data_alter_reporting_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='email',
        ),
    ]