# Generated by Django 3.2.6 on 2022-04-13 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_currency_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='banner',
            field=models.ImageField(default=0, upload_to='profile'),
            preserve_default=False,
        ),
    ]
