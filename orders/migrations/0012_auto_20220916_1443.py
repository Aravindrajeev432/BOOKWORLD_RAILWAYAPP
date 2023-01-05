# Generated by Django 3.1 on 2022-09-16 09:13

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_image',
            field=image_cropping.fields.ImageCropField(blank=True, upload_to='photos/banner'),
        ),
    ]
