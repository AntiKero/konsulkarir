# Generated by Django 2.2.14 on 2020-08-09 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0002_auto_20200809_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='area',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
