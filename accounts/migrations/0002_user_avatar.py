# Generated by Django 3.2.3 on 2021-05-19 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, help_text='Profile picture', null=True, upload_to='', verbose_name='avatar'),
        ),
    ]
