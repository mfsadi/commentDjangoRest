# Generated by Django 3.0.4 on 2020-03-07 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentManager', '0002_auto_20200307_1910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_id',
            new_name='post',
        ),
    ]
