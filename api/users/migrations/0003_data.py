# Generated by Django 3.0.8 on 2020-08-01 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171227_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=40)),
                ('transaction_date', models.CharField(max_length=10)),
                ('transaction_amount', models.PositiveIntegerField()),
                ('client_id', models.PositiveIntegerField()),
                ('client_name', models.CharField(max_length=100)),
            ],
        ),
    ]