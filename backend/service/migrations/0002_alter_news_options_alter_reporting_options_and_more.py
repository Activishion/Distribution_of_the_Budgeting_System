# Generated by Django 4.2 on 2023-04-26 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'новость', 'verbose_name_plural': 'новости'},
        ),
        migrations.AlterModelOptions(
            name='reporting',
            options={'verbose_name': 'подписку', 'verbose_name_plural': 'подписки'},
        ),
        migrations.RenameField(
            model_name='reporting',
            old_name='email',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='message',
            name='DZO',
            field=models.BooleanField(default=True, verbose_name='ДЗО'),
        ),
        migrations.AlterField(
            model_name='message',
            name='PAO',
            field=models.BooleanField(default=True, verbose_name='ПАО'),
        ),
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Отправитель'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(verbose_name='Текст сообщения'),
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='reporting',
            name='report',
            field=models.CharField(choices=[('RTK', 'Прибыли и убытки РТК'), ('TEL', 'РТК + Tele2'), ('REP', 'Сегментная отчетность')], max_length=100, verbose_name='Отчет'),
        ),
    ]