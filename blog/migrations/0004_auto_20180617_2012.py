# Generated by Django 2.0.6 on 2018-06-17 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180617_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='images/',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='0', upload_to='images/'),
            preserve_default=False,
        ),
    ]