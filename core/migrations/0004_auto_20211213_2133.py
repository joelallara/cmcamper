# Generated by Django 3.1.7 on 2021-12-14 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_galeriamotorhome_galeriaoffroad_galeriapopup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galeriamotorhome',
            options={'ordering': ['orden'], 'verbose_name': 'Galeria MotorHome', 'verbose_name_plural': 'Galeria MotorHome'},
        ),
        migrations.AlterModelOptions(
            name='galeriaoffroad',
            options={'ordering': ['orden'], 'verbose_name': 'Galeria OffRoad', 'verbose_name_plural': 'Galeria OffRoad'},
        ),
        migrations.AlterModelOptions(
            name='galeriapopup',
            options={'ordering': ['orden'], 'verbose_name': 'Galeria Popup', 'verbose_name_plural': 'Galeria Popup'},
        ),
        migrations.AlterModelOptions(
            name='galeriaproductos',
            options={'ordering': ['orden'], 'verbose_name': 'Galeria Productos', 'verbose_name_plural': 'Galeria Productos'},
        ),
        migrations.AddField(
            model_name='contacto',
            name='link_instagram',
            field=models.URLField(blank=True, null=True),
        ),
    ]
