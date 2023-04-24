# Generated by Django 4.2 on 2023-04-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, to='auth.group'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, null=True, to='auth.permission'),
        ),
    ]
