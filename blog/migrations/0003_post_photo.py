# Generated by Django 2.0.4 on 2018-04-06 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.URLField(blank=True),
        ),
    ]
