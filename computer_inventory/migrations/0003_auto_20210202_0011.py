# Generated by Django 3.1.5 on 2021-02-02 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer_inventory', '0002_auto_20210202_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='model_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='person_full_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='serial_number',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='user_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]