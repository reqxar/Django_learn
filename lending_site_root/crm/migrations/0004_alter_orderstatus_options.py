# Generated by Django 3.2.6 on 2021-08-10 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20210810_1918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderstatus',
            options={'verbose_name': 'Cтатус', 'verbose_name_plural': 'Статусы'},
        ),
    ]
