# Generated by Django 3.0.5 on 2020-04-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Letters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letters_uz',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
