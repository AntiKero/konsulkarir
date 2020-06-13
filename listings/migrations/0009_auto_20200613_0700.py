# Generated by Django 2.2.11 on 2020-06-13 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20200427_0402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='tags',
            field=models.ManyToManyField(to='listings.Tag'),
        ),
    ]
