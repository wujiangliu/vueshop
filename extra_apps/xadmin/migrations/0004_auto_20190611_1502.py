# Generated by Django 2.0 on 2019-06-11 07:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xadmin', '0003_auto_20160715_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='content_type',
            field=models.ForeignKey(on_delete='CASCADE', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='user',
            field=models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='userwidget',
            name='user',
            field=models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]