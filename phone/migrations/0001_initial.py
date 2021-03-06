# Generated by Django 3.1.7 on 2021-03-20 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('phone_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=10)),
                ('middle_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='CallHistoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('phone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_call_id', to='phone.phonemodel')),
            ],
        ),
    ]
