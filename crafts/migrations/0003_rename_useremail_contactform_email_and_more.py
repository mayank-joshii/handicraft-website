# Generated by Django 5.0 on 2024-02-27 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crafts', '0002_contactform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='userEmail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contactform',
            old_name='userName',
            new_name='name',
        ),
    ]
