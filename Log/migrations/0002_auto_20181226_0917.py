# Generated by Django 2.1.4 on 2018-12-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
