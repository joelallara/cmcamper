# Generated by Django 3.1.7 on 2023-05-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_sobrenosotros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sobrenosotros',
            name='descripcion',
            field=models.TextField(),
        ),
    ]