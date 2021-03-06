# Generated by Django 3.2 on 2021-04-23 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Racer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('avatar', models.ImageField(upload_to='')),
                ('info', models.TextField(blank=True)),
                ('target', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Wager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('race', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.race')),
                ('racer1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topdog_racer', to='core.racer')),
                ('racer2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='underdog_racer', to='core.racer')),
            ],
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stake', models.TextField()),
                ('place', models.CharField(choices=[('t', 'Initializing'), ('u', 'Outsider')], default='t', max_length=1)),
                ('status', models.CharField(choices=[('i', 'Initializing'), ('d', 'Done'), ('c', 'Cancelled')], default='i', max_length=3)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
