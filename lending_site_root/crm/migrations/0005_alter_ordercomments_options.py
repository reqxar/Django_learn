# Generated by Django 3.2.6 on 2021-08-10 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_alter_orderstatus_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordercomments',
            options={'verbose_name': 'Комметарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
