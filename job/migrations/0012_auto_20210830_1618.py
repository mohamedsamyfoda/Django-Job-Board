# Generated by Django 3.0.7 on 2021-08-30 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_auto_20210830_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]