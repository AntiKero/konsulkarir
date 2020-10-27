# Generated by Django 2.2.14 on 2020-08-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0004_vacancy_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='post_picture',
            field=models.ImageField(blank=True, upload_to='jobportal/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='picture',
            field=models.ImageField(upload_to='jobportal/%Y/%m/%d/'),
        ),
    ]