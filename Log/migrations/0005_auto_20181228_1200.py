# Generated by Django 2.1.4 on 2018-12-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0004_auto_20181226_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
