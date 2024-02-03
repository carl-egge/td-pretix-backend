# Generated by Django 4.2.9 on 2024-02-03 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0255_merge_20240203_1406'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='reusablemedium',
            index_together=set(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='locale',
            field=models.CharField(default='en', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='locale',
            field=models.CharField(default='en', max_length=50),
        ),
    ]
