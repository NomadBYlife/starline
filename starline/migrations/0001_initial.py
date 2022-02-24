# Generated by Django 4.0.2 on 2022-02-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NumberPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='', verbose_name='Логотип оператора связи')),
                ('numbers', models.CharField(max_length=50, verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='OurWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='', verbose_name='Фотографии работ')),
                ('video_url', models.CharField(max_length=200, verbose_name='Видео работ')),
            ],
        ),
        migrations.CreateModel(
            name='Warranty_Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Гарантия и поддержка')),
            ],
        ),
    ]