# Generated by Django 4.0.6 on 2022-08-12 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_rename_question_map_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GoogleMap_Image',
        ),
    ]
