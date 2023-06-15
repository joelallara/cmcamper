# Generated by Django 3.1.7 on 2023-06-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20230522_2115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portada',
            options={'ordering': ['orden'], 'verbose_name': 'Portada', 'verbose_name_plural': 'Portada'},
        ),
        migrations.AddField(
            model_name='portada',
            name='url_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
