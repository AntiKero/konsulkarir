# Generated by Django 2.2.11 on 2020-04-03 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0005_auto_20200404_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultant',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
