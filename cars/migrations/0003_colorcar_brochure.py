# Generated by Django 4.2.2 on 2023-07-01 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_carmodel_cartype'),
    ]

    operations = [
        migrations.AddField(
            model_name='colorcar',
            name='brochure',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cars.brochure'),
            preserve_default=False,
        ),
    ]