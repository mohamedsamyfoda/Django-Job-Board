# Generated by Django 3.0.7 on 2021-08-31 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='modelNum',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='modelTime',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]