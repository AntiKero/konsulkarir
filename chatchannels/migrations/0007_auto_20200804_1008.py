# Generated by Django 2.2.14 on 2020-08-04 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatchannels', '0006_auto_20200802_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='chats',
            new_name='chat',
        ),
    ]
