# Generated by Django 3.1.7 on 2021-03-07 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transmission', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('traction', models.CharField(max_length=100)),
                ('hpower', models.CharField(max_length=100)),
                ('motor', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('fuel', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('km', models.IntegerField()),
                ('color', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('year_purch', models.IntegerField()),
                ('carinfo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car_info')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
