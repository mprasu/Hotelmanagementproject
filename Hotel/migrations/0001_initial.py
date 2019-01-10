# Generated by Django 2.1 on 2018-10-17 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelSuprabat',
            fields=[
                ('roomnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('roomtype', models.CharField(max_length=50)),
                ('aminity', models.CharField(max_length=8)),
                ('cost', models.DecimalField(decimal_places=4, max_digits=10)),
                ('booked', models.CharField(max_length=5)),
            ],
        ),
    ]
