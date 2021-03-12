# Generated by Django 3.1.7 on 2021-03-12 07:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bike',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='bike',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]