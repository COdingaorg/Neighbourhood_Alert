# Generated by Django 3.2.4 on 2021-07-25 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoodalert', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('location', models.TextField()),
                ('population', models.IntegerField()),
                ('admin_user_prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodalert.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodalert.neighbourhood')),
                ('user_prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodalert.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodalert.neighbourhood')),
                ('user_prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodalert.userprofile')),
            ],
        ),
    ]
