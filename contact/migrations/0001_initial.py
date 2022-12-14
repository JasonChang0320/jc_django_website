# Generated by Django 4.0.6 on 2022-08-11 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='公司名稱')),
                ('title', models.CharField(max_length=20, verbose_name='標題')),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='電話:')),
                ('email', models.CharField(blank=True, max_length=60, verbose_name='E-mail')),
                ('adress', models.TextField(blank=True, max_length=100, verbose_name='地址')),
                ('office_hour', models.CharField(blank=True, max_length=60, verbose_name='辦公時間')),
            ],
        ),
    ]
