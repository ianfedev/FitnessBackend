# Generated by Django 3.0.6 on 2020-05-30 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]