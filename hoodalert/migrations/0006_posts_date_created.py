# Generated by Django 3.2.4 on 2021-07-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodalert', '0005_alter_posts_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='date_created',
            field=models.DateTimeField(null=True),
        ),
    ]