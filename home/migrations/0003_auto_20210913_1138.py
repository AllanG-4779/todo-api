# Generated by Django 3.2.7 on 2021-09-13 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_items_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='completed_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
