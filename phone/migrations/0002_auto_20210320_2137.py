# Generated by Django 3.1.7 on 2021-03-20 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='middle_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
