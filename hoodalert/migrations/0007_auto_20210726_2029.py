# Generated by Django 3.2.4 on 2021-07-26 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoodalert', '0006_posts_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='healthdep',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='policedep',
            options={'ordering': ['-id']},
        ),
    ]
