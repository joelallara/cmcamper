# Generated by Django 3.1.7 on 2023-05-23 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20230522_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galeriamotorhome',
            name='titulo_card',
        ),
        migrations.RemoveField(
            model_name='galeriaoffroad',
            name='titulo_card',
        ),
        migrations.RemoveField(
            model_name='galeriapopup',
            name='titulo_card',
        ),
    ]