# Generated by Django 4.2.2 on 2023-07-01 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='cartype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cars.transporttype'),
            preserve_default=False,
        ),
    ]
