# Generated by Django 3.1.5 on 2021-05-04 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INED_app', '0003_auto_20210504_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Sube una fotografía'),
        ),
    ]