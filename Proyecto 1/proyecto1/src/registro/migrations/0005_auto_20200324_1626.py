# Generated by Django 3.0.4 on 2020-03-24 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_auto_20200323_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resena',
            old_name='reseña',
            new_name='resena',
        ),
        migrations.AddField(
            model_name='registrado',
            name='password',
            field=models.CharField(default='SOME STRING', max_length=140),
        ),
        migrations.AddField(
            model_name='registrado',
            name='usuario',
            field=models.CharField(default='SOME STRING', max_length=70, unique=True),
        ),
    ]