# Generated by Django 3.0.4 on 2020-03-07 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentManager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='post_id',
        ),
    ]
