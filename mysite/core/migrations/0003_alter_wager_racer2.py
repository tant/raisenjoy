# Generated by Django 3.2 on 2021-04-23 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_bet_racer_wager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wager',
            name='racer2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='underdog_racer', to='core.racer'),
        ),
    ]