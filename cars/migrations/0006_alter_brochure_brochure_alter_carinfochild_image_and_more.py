# Generated by Django 4.2.2 on 2023-07-01 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_carmodel_car_description_alter_carmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brochure',
            name='brochure',
            field=models.FileField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='carinfochild',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='car_image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='colorcar',
            name='car_image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
