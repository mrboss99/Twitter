# Generated by Django 2.1.4 on 2018-12-26 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0002_auto_20181226_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, default=0, null=True),
        ),
    ]
