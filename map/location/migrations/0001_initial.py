# Generated by Django 3.2.6 on 2022-04-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='locate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True)),
            ],
        ),
    ]
