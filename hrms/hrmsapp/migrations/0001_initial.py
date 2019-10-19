# Generated by Django 2.2.6 on 2019-10-19 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=100)),
                ('guest_address', models.TextField()),
                ('guest_phone', models.IntegerField()),
                ('guest_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('hotel_location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_name', models.CharField(max_length=100)),
                ('manager_phone', models.IntegerField()),
                ('manager_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='room_type_name')),
                ('room_rent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField(default=101)),
                ('availability', models.BooleanField(default=False)),
                ('bed_number', models.IntegerField(default=2)),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrmsapp.RoomType')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('checked_in', models.BooleanField(default=False)),
                ('cancel', models.BooleanField(default=False)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrmsapp.Guest')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrmsapp.Manager')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrmsapp.Room')),
            ],
        ),
    ]
