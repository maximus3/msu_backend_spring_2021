# Generated by Django 3.2 on 2021-05-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='chats',
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Возраст'),
        ),
    ]
