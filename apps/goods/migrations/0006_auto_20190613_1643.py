# Generated by Django 2.0 on 2019-06-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20190611_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategory',
            name='category_type',
            field=models.CharField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], help_text='类目级别', max_length=20, verbose_name='类目级别'),
        ),
    ]
