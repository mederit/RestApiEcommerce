# Generated by Django 3.1.7 on 2021-03-12 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210312_0810'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='bike_images')),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.bike')),
            ],
        ),
    ]
