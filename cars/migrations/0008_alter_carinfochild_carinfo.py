# Generated by Django 4.2.2 on 2023-07-03 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_brochure_carmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carinfochild',
            name='carinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carchild', to='cars.carinfo'),
        ),
    ]