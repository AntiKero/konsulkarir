# Generated by Django 2.2.14 on 2020-08-02 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatchannels', '0003_auto_20200802_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='chats',
        ),
        migrations.AddField(
            model_name='message',
            name='chats',
            field=models.ManyToManyField(default='', to='chatchannels.Chat'),
        ),
    ]
