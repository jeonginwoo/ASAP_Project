# Generated by Django 4.2.4 on 2023-08-15 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0009_rename_a_chicken_menutable_a_chicken_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menutable',
            name='image',
            field=models.ImageField(blank=True, max_length=50, null=True, upload_to='', verbose_name='이미지'),
        ),
    ]