# Generated by Django 2.2.14 on 2020-08-09 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0003_vacancy_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='vacancy', to='jobportal.Company'),
            preserve_default=False,
        ),
    ]