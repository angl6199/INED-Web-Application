# Generated by Django 3.1.5 on 2021-05-04 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INED_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='staff',
            field=models.BooleanField(default=True),
        ),
    ]
