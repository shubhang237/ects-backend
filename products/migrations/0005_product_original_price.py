# Generated by Django 2.1.5 on 2020-03-31 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200331_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='original_price',
            field=models.FloatField(default=250),
            preserve_default=False,
        ),
    ]
