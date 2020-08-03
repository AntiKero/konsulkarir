# Generated by Django 2.2.14 on 2020-08-02 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatchannels', '0002_message_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='chat',
        ),
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant1', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user1', to=settings.AUTH_USER_MODEL)),
                ('participant2', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='chats',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='chatchannels.Chat'),
        ),
    ]
