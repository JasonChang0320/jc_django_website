# Generated by Django 4.0.6 on 2022-10-05 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_experience_en_service_en_service_title_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='content',
            field=models.TextField(blank=True, max_length=500, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='title',
            field=models.CharField(max_length=50, verbose_name='委託單位'),
        ),
    ]