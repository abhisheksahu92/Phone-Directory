# Generated by Django 3.1.7 on 2021-05-04 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0003_auto_20210321_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='callhistorymodel',
            name='duration',
            field=models.DurationField(null=True),
        ),
    ]
