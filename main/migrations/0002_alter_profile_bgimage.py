# Generated by Django 4.2.4 on 2025-03-30 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bgimage',
            field=models.ImageField(default='bg.png', upload_to='bg_image'),
        ),
    ]
