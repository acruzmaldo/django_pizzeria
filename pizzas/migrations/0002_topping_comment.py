# Generated by Django 3.0.5 on 2022-12-12 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topping',
            name='comment',
            field=models.CharField(default='No Comments', max_length=300),
        ),
    ]
