# Generated by Django 3.1 on 2022-09-05 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_order_coupon'),
    ]

    operations = [
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.ImageField(blank=True, upload_to='photos/banner')),
                ('is_selected', models.BooleanField(default=False)),
            ],
        ),
    ]
