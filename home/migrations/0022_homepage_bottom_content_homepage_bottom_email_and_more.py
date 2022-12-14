# Generated by Django 4.0.6 on 2022-08-16 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_homepage_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='bottom_content',
            field=models.TextField(blank=True, max_length=300, verbose_name='底部內容'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='bottom_email',
            field=models.CharField(blank=True, max_length=100, verbose_name='底部email'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='bottom_phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='底部連絡電話'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='bottom_title',
            field=models.CharField(blank=True, max_length=20, verbose_name='底部標題'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sub_title1',
            field=models.CharField(blank=True, max_length=50, verbose_name='子標題1'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sub_title2',
            field=models.CharField(blank=True, max_length=50, verbose_name='子標題2'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sub_title3',
            field=models.CharField(blank=True, max_length=50, verbose_name='子標題3'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sub_title4',
            field=models.CharField(blank=True, max_length=50, verbose_name='子標題4'),
        ),
    ]
