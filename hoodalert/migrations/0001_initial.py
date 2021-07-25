# Generated by Django 3.2.4 on 2021-07-25 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthDep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('contact', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('location', models.TextField()),
                ('population', models.IntegerField()),
                ('health_dep', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodalert.healthdep')),
            ],
        ),
        migrations.CreateModel(
            name='PoliceDep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('contact', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_path', models.ImageField(upload_to='profiles/')),
                ('about', models.CharField(max_length=200)),
                ('location_description', models.TextField(null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('hood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodalert.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='police_dep',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodalert.policedep'),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.TextField()),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodalert.neighbourhood')),
                ('owner_user_prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodalert.userprofile')),
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
