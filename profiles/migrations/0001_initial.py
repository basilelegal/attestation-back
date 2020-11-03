# Generated by Django 3.1.3 on 2020-11-02 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(max_length=50, verbose_name='Nom du profil')),
                ('firstname', models.CharField(max_length=255, verbose_name='Prénom')),
                ('lastname', models.CharField(max_length=255, verbose_name='Nom')),
                ('birthdate', models.DateField(verbose_name='Date de naissance')),
                ('birthplace', models.CharField(max_length=255, verbose_name='Lieu de naissance')),
                ('address', models.CharField(max_length=2047, verbose_name='Adresse')),
                ('city', models.CharField(max_length=255, verbose_name='Ville')),
                ('zipcode', models.CharField(max_length=255, verbose_name='Code postal')),
            ],
        ),
    ]