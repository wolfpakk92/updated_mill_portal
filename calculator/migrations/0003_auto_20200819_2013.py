# Generated by Django 3.1 on 2020-08-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_auto_20200818_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipename',
            name='type',
        ),
        migrations.AddField(
            model_name='recipename',
            name='recipe_type',
            field=models.CharField(default='NORR', max_length=16),
        ),
        migrations.AlterField(
            model_name='recipeconcentration',
            name='recipe_type',
            field=models.CharField(default='NORR', max_length=16),
        ),
    ]