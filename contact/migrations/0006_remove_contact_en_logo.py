# Generated by Django 4.0.6 on 2022-08-23 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_contact_en'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_en',
            name='logo',
        ),
    ]
