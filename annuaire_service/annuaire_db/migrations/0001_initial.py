# Generated by Django 4.2.9 on 2024-01-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('user_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'annuaire_db_contact',
            },
        ),
    ]
