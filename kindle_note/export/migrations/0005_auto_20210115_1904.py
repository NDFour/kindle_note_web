# Generated by Django 2.2 on 2021-01-15 11:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('export', '0004_auto_20200912_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload_record',
            name='export_info',
        ),
        migrations.RemoveField(
            model_name='upload_record',
            name='mail_addr',
        ),
        migrations.RemoveField(
            model_name='upload_record',
            name='mail_state',
        ),
        migrations.AddField(
            model_name='upload_record',
            name='download_status',
            field=models.CharField(default='空', max_length=255, verbose_name='下载状态'),
        ),
        migrations.AddField(
            model_name='upload_record',
            name='download_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 15, 11, 4, 34, 50819, tzinfo=utc), verbose_name='下载时间'),
        ),
        migrations.AddField(
            model_name='upload_record',
            name='export_status',
            field=models.CharField(default='空', max_length=255, verbose_name='转换状态'),
        ),
        migrations.AddField(
            model_name='upload_record',
            name='is_export_anki',
            field=models.IntegerField(blank=True, default=0, verbose_name='导出 Anki'),
        ),
        migrations.AlterField(
            model_name='upload_record',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 15, 11, 4, 34, 50776, tzinfo=utc), verbose_name='上传时间'),
        ),
    ]