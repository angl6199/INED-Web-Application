# Generated by Django 3.1.5 on 2021-05-15 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INED_app', '0005_auto_20210515_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo_contratacion',
            field=models.CharField(choices=[('Estructura', 'Estructura'), ('Nomina 8', 'Nomina 8'), ('Honorarios', 'Honorarios'), ('Base con digito sindical', 'Base con digito sindical'), ('Base sin digito sindical', 'Base sin digito sindical')], max_length=50, verbose_name='Tipo de contratación'),
        ),
    ]
