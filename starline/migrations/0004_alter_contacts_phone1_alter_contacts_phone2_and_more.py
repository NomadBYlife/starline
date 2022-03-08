# Generated by Django 4.0.2 on 2022-03-03 15:17

from django.db import migrations, models
import starline.models


class Migration(migrations.Migration):

    dependencies = [
        ('starline', '0003_category_security_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='phone1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер телефона 1'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер телефона 2'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='phone',
            field=models.CharField(max_length=50, validators=[starline.models.validate_phone], verbose_name='Телефон'),
        ),
    ]
