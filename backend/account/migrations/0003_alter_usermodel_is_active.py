# Generated by Django 4.2 on 2023-04-24 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_usermodel_groups_alter_usermodel_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
