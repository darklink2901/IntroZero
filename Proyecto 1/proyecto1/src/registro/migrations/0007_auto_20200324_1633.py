# Generated by Django 3.0.4 on 2020-03-24 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0006_auto_20200324_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrado',
            name='password',
            field=models.CharField(max_length=140),
        ),
    ]
