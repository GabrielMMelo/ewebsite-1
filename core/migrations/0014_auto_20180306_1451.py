# Generated by Django 2.0.2 on 2018-03-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_equipe_sobre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='sobre',
            field=models.TextField(),
        ),
    ]