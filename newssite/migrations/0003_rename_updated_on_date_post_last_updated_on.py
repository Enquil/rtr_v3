# Generated by Django 3.2.19 on 2023-06-29 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newssite', '0002_auto_20230629_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='updated_on_date',
            new_name='last_updated_on',
        ),
    ]