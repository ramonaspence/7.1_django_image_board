# Generated by Django 4.0.2 on 2022-02-07 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_painting_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
