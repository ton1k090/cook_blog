# Generated by Django 4.1.7 on 2023-03-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_about_social_imageabout'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]