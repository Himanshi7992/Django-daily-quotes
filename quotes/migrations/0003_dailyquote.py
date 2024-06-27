# Generated by Django 5.0.6 on 2024-06-26 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_rename_quote_quotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_year', models.PositiveIntegerField(unique=True)),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.quotes')),
            ],
        ),
    ]
