# Generated by Django 2.1.5 on 2020-03-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=250),
            preserve_default=False,
        ),
    ]