# Generated by Django 2.2.14 on 2020-08-24 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatchannels', '0009_auto_20200824_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='participant1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chat',
            name='participant2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user2', to=settings.AUTH_USER_MODEL),
        ),
    ]