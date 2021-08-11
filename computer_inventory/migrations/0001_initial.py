# Generated by Django 3.1.5 on 2021-01-30 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operating_system', models.CharField(choices=[('WIN10', 'WINDOWS 10'), ('WIN7', 'WINDOWS 7')], default='WIN10', max_length=5)),
                ('computer_name', models.CharField(blank=True, max_length=7, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=7, null=True)),
                ('user_name', models.CharField(blank=True, max_length=30, null=True)),
                ('person_full_name', models.CharField(blank=True, max_length=40, null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('model_number', models.CharField(blank=True, max_length=10, null=True)),
                ('location', models.CharField(choices=[('SILVER 4', 'SILVER 4'), ('SILVER5', 'SILVER 5'), ('SILVER 6', 'SILVER 6'), ('WHITE 6', 'WHITE 6'), ('PRESBY', 'PRESBY'), ('PCAM3', 'PCAM3'), ('PCAM4', 'PCAM4'), ('GATES5', 'GATES 5'), ('GROUND FOUNDERS 013', 'GROUND FOUNDERS 013'), ('GROUN', 'GROUND FOUNDER 079'), ('STEMMLER HALL', 'STEMMLER HALL'), ('RAV 5 COURTYARD', 'RAV 5 COURTYARD'), ('DULLES 2', 'DULLES 2'), ('DULLES 2 COURT', 'DULLES 2 COURT'), ('SILVER5', 'SILVER5'), ('1500 MARKET ST', '1500 MARKET ST'), ('SPE1', 'SPE1'), ('SPE14', 'SPE14'), ('SPE10', 'SPE10'), ('MALONEY 5', 'MALONEY 5'), ('MALONEY 4', 'MALONEY 4')], max_length=19, null=True)),
                ('comments', models.CharField(blank=True, max_length=30, null=True)),
                ('export_to_CSV', models.BooleanField(default=False)),
            ],
        ),
    ]