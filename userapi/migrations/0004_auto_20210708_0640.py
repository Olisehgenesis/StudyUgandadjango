# Generated by Django 3.1.7 on 2021-07-08 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0003_auto_20210708_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='school',
            field=models.CharField(max_length=100),
        ),
    ]