# Generated by Django 3.2.7 on 2022-02-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0006_aula_vimeo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='vimeo_id',
            field=models.CharField(max_length=32),
        ),
    ]