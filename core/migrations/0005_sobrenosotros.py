# Generated by Django 3.1.7 on 2023-05-06 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211213_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='SobreNosotros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Sobre Nosotros',
                'verbose_name_plural': 'Sobre Nosotros',
            },
        ),
    ]