# Generated by Django 3.1.5 on 2021-02-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer_inventory', '0004_auto_20210202_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='model_number',
            field=models.CharField(choices=[('T410', 'T410'), ('T420', 'T420'), ('T440', 'T440'), ('T460', 'T460'), ('T470', 'T470'), ('T480', 'T480'), ('T490', 'T490'), ('CARBON', 'CARBON'), ('SURFACE LAPTOP', 'SURFACE LAPTOP'), ('T14S', 'T14S'), ('10AF', '10AF'), ('10AE', '10AE'), ('10NS', '10NS'), ('10F5', '10F5'), ('10S6', '10S6'), ('10S7', '10S7'), ('3318', '3318'), ('3391', '3391'), ('10ML', '10ML'), ('5205', '5205'), ('0870', '0870'), ('MINI', 'MINI'), ('OTHER', 'OTHER')], max_length=14, null=True),
        ),
    ]