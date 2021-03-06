# Generated by Django 2.2.14 on 2020-08-09 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('jobportal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='company', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('website', models.CharField(blank=True, max_length=200)),
                ('company_size', models.IntegerField()),
                ('industry', models.CharField(max_length=200)),
                ('overview', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='content',
            new_name='description',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='experience_required',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='salary',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='specialization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='vacancy', to='jobportal.Specialization'),
            preserve_default=False,
        ),
    ]
