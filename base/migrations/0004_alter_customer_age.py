# Generated by Django 5.0.1 on 2024-01-21 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
