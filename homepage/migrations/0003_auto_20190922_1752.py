# Generated by Django 2.1.1 on 2019-09-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20190922_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='name',
            field=models.CharField(max_length=400),
        ),
    ]
