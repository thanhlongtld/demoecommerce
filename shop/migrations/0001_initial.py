# Generated by Django 4.0.2 on 2022-02-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('thumbnail', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
