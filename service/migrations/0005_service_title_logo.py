# Generated by Django 4.0.6 on 2022-08-16 07:24

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_service_title_bottom_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_title',
            name='logo',
            field=models.ImageField(blank=True, storage=home.models.OverwriteStorage(), upload_to='', verbose_name='公司logo'),
        ),
    ]