# Generated by Django 3.0.7 on 2021-08-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_auto_20210830_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='title',
        ),
        migrations.AddField(
            model_name='job',
            name='des',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]