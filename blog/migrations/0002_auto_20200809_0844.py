# Generated by Django 2.2.14 on 2020-08-09 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, upload_to='blogpic/%Y/%m/%d/'),
        ),
    ]