# Generated by Django 2.2.3 on 2020-01-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sih_app', '0005_alumni_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
