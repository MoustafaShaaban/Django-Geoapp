# Generated by Django 4.0.10 on 2023-03-01 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Feature Name', max_length=250)),
                ('description', models.TextField(help_text='Feature Description')),
                ('type', models.CharField(help_text='Feature Type (Hotel, Hospital, School, Park, ...)', max_length=100)),
                ('latitude', models.FloatField(help_text='Latitude')),
                ('longitude', models.FloatField(help_text='Longitude')),
            ],
            options={
                'verbose_name': 'feature',
                'verbose_name_plural': 'features',
            },
        ),
    ]