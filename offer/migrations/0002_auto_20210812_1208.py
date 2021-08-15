# Generated by Django 3.2.6 on 2021-08-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='file',
            field=models.FileField(blank=True, upload_to='', verbose_name='Памятка'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='text',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
