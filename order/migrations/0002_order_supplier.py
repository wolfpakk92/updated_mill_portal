# Generated by Django 3.1 on 2021-02-08 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier'),
        ),
    ]
